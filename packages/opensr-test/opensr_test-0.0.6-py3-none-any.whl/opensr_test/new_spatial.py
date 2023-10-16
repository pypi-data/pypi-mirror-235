import itertools
import warnings
from typing import Dict, Optional, Tuple, Union, List

import numpy as np
import torch
from opensr_test.lightglue import DISK, LightGlue, SuperPoint
from opensr_test.lightglue.utils import rbd
from opensr_test.utils import Value, hq_histogram_matching, spectral_reducer
from scipy.spatial.distance import cdist
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import PolynomialFeatures


def distance_matrix(
    x0: np.ndarray, y0: np.ndarray, x1: np.ndarray, y1: np.ndarray
) -> np.ndarray:
    """Calculate the distance matrix between two sets of points

    Args:
        x0 (np.ndarray): Array with the x coordinates of the points (image 1)
        y0 (np.ndarray): Array with the y coordinates of the points (image 1)
        x1 (np.ndarray): Array with the x coordinates of the points (image 2)
        y1 (np.ndarray): Array with the y coordinates of the points (image 2)

    Returns:
        np.ndarray: Array with the distances between the points
    """
    obs = np.vstack((x0, y0)).T
    interp = np.vstack((x1, y1)).T
    return cdist(obs, interp)


def linear_rbf(
    x: np.ndarray, y: np.ndarray, z: np.ndarray, xi: np.ndarray, yi: np.ndarray
) -> np.ndarray:
    """Interpolate using radial basis functions

    Args:
        x (np.ndarray): Array with the x coordinates of the points (image 1)
        y (np.ndarray): Array with the y coordinates of the points (image 1)
        z (np.ndarray): Array with the z coordinates of the points (image 1)
        xi (np.ndarray): Array with the x coordinates of the points (target image)
        yi (np.ndarray): Array with the y coordinates of the points (target image)
    
    Returns:
        np.ndarray: Array with the interpolated values
    """
    dist = distance_matrix(x, y, xi, yi)

    # Mutual pariwise distances between observations
    internal_dist = distance_matrix(x, y, x, y)

    # Now solve for the weights such that mistfit at the observations is minimized
    weights = np.linalg.solve(internal_dist, z)

    # Multiply the weights for each interpolated point by the distances
    zi = np.dot(dist.T, weights)

    return zi

def spatia_polynomial_fit(X: np.ndarray, y: np.ndarray, d: int) -> Pipeline:
    """Fit a polynomial of degree d to the points

    Args:
        X (np.ndarray): Array with the x coordinates or y coordinates of the points (image 1)
        y (np.ndarray): Array with the x coordinates or y coordinates of the points (image 2)
        d (int): Degree of the polynomial

    Returns:
        Pipeline: The fitted model
    """

    pipe_model = make_pipeline(
        PolynomialFeatures(degree=d, include_bias=False), LinearRegression()
    ).fit(X, y)

    return pipe_model


def spatial_setup_model(
    features: str = "superpoint",
    matcher: str = "lightglue",
    max_num_keypoints: int = 2048,
    device: str = "cpu",
) -> tuple:
    """Setup the model for spatial check

    Args:
        features (str, optional): The feature extractor. Defaults to 'superpoint'.
        matcher (str, optional): The matcher. Defaults to 'lightglue'.
        max_num_keypoints (int, optional): The maximum number of keypoints. Defaults to 2048.
        device (str, optional): The device to use. Defaults to 'cpu'.

    Raises:
        ValueError: If the feature extractor or the matcher are not valid
        ValueError: If the device is not valid

    Returns:
        tuple: The feature extractor and the matcher models
    """

    # Local feature extractor
    if features == "superpoint":
        extractor = SuperPoint(max_num_keypoints=max_num_keypoints).eval().to(device)
    elif features == "disk":
        extractor = DISK(max_num_keypoints=max_num_keypoints).eval().to(device)
    else:
        raise ValueError(f"Unknown feature extractor {features}")

    # Local feature matcher
    if matcher == "lightglue":
        matcher = LightGlue(features=features).eval().to(device)
    else:
        raise ValueError(f"Unknown matcher {matcher}")

    return extractor, matcher


def spatial_get_matching_points(
    img01: torch.Tensor,
    img02: torch.Tensor,
    model: tuple, 
    spectral_reducer_method: str,
    rgb_bands: List[int],
    device: str = "cpu",
) -> Dict[str, torch.Tensor]:
    """Predict the spatial error between two images

    Args:
        img01 (torch.Tensor): A torch.tensor with the image 1 (B, H, W)
        img02 (torch.Tensor): A torch.tensor with the ref image (B, H, W)
        model (tuple): A tuple with the feature extractor and the matcher
        device (str, optional): The device to use. Defaults to 'cpu'.

    Returns:
        Dict[str, torch.Tensor]: A dictionary with the points0, 
            points1, matches01 and image size.
    """

    # unpack the model - send to device
    extractor, matcher = model
    extractor = extractor.to(device)
    matcher = matcher.to(device)

    # Send the data to the device
    img01 = spectral_reducer(
        X=img01.to(device),
        method=spectral_reducer_method,
        rgb_bands=rgb_bands
    )[None]
    
    img02 = spectral_reducer(
        X=img02.to(device),
        method=spectral_reducer_method,
        rgb_bands=rgb_bands
    )[None]

    # extract local features
    with torch.no_grad():
        # auto-resize the image, disable with resize=None
        feats0 = extractor.extract(img01, resize=None)
        if feats0["keypoints"].shape[1] == 0:
            warnings.warn("No keypoints found in image 1")
            return False

        feats1 = extractor.extract(img02, resize=None)
        if feats1["keypoints"].shape[1] == 0:
            warnings.warn("No keypoints found in image 2")
            return False

        # match the features
        matches01 = matcher({"image0": feats0, "image1": feats1})

    # remove batch dimension
    feats0, feats1, matches01 = [rbd(x) for x in [feats0, feats1, matches01]]

    matches = matches01["matches"]  # indices with shape (K,2)
    points0 = feats0["keypoints"][
        matches[..., 0]
    ]  # coordinates in image #0, shape (K,2)
    points1 = feats1["keypoints"][
        matches[..., 1]
    ]  # coordinates in image #1, shape (K,2)

    matching_points = {
        "points0": points0,
        "points1": points1,
        "matches01": matches01,
        "img_size": tuple(img01.shape[-2:]),
    }

    return matching_points

def spatial_model_fit(
    matching_points: Dict[str, torch.Tensor],
    n_points: Optional[int] = 10,
    threshold_distance: Optional[int] = 5,
    verbose: Optional[bool] = True
) -> Union[np.ndarray, dict]:
    """Get a model that minimizes the spatial error between two images

    Args:
        matching_points (Dict[str, torch.Tensor]): A dictionary with the points0, 
            points1 and image size.
        n_points (Optional[int], optional): The minimum number of points. Defaults
            to 10.
        threshold_distance (Optional[int], optional): The maximum distance between
            the points. Defaults to 5 pixels.
        verbose (Optional[bool], optional): If True, print the error. Defaults to
            False.
        scale (Optional[int], optional): The scale factor to use. Defaults to 1.
        
    Returns:
        np.ndarray: The spatial error between the two images
    """

    points0 = matching_points["points0"]
    points1 = matching_points["points1"]

    # if the distance between the points is higher than 5 pixels,
    # it is considered a bad match
    dist = torch.sqrt(torch.sum((points0 - points1) ** 2, dim=1))
    thres = dist < threshold_distance
    p0 = points0[thres]
    p1 = points1[thres]

    # if not enough points, return 0
    if p0.shape[0] < n_points:
        warnings.warn("Not enough points to fit the model")
        return False

    # from torch.Tensor to numpy array
    p0 = p0.detach().cpu().numpy()
    p1 = p1.detach().cpu().numpy()

    # Fit a polynomial of degree 2 to the points
    X_img0 = p0[:, 0].reshape(-1, 1)
    X_img1 = p1[:, 0].reshape(-1, 1)
    model_x = spatia_polynomial_fit(X_img0, X_img1, 1)

    y_img0 = p0[:, 1].reshape(-1, 1)
    y_img1 = p1[:, 1].reshape(-1, 1)
    model_y = spatia_polynomial_fit(y_img0, y_img1, 1)

    # display error
    xoffset = np.round(model_x.predict(np.array(0).reshape(-1, 1)))
    yoffset = np.round(model_y.predict(np.array(0).reshape(-1, 1)))

    xhat = X_img0 + xoffset
    yhat = y_img0 + yoffset

    # full error
    full_error1 = np.sqrt((xhat - X_img1) ** 2 + (yhat - y_img1) ** 2)
    full_error2 = np.sqrt((X_img0 - X_img1) ** 2 + (y_img0 - y_img1) ** 2)

    if verbose:
        print(f"Initial [RMSE]: %.04f" % np.mean(full_error2))
        print(f"Final [RMSE]: %.04f" % np.mean(full_error1))

    to_export = {
        "offset": (int(xoffset), int(yoffset)),
        "error": (np.mean(full_error2), np.mean(full_error1)),
    }

    return to_export


def spatial_model_transform_pixel(
    image1: torch.Tensor,
    spatial_offset: tuple,
) -> torch.Tensor:
    """ Transform the image according to the spatial offset

    Args:
        image1 (torch.Tensor): The image 1 with shape (B, H, W)
        spatial_offset (tuple): The spatial offset estimated by the 
            spatial_model_fit function.
    Returns:
        torch.Tensor: The transformed image
    """
    x_offs, y_offs = spatial_offset["offset"]

    # get max offset
    moffs = np.max(np.abs([x_offs, y_offs]))

    
    # Add padding according to the offset
    image_pad = torch.nn.functional.pad(
        image1, (moffs, moffs, moffs, moffs), mode="constant", value=0
    )
    
    if x_offs < 0:
        image_pad = image_pad[:, :, (moffs + x_offs) :]
    elif x_offs > 0:
        image_pad = image_pad[:, :, (moffs - x_offs) :]
    
    if y_offs < 0:
        image_pad = image_pad[:, (moffs - y_offs) :, :]
    elif y_offs > 0:
        image_pad = image_pad[:, (moffs + y_offs) :, :]
    
    # remove padding
    final_image = image_pad[:, 0:image1.shape[1], 0:image1.shape[2]]
    
    return final_image

def spatial_model_transform(
    lr_to_hr: torch.Tensor,
    hr: torch.Tensor,
    spatial_offset: tuple
) -> torch.Tensor:
    """ Transform the image according to the spatial offset

    Args:
        lr_to_hr (torch.Tensor): The low resolution image
        hr (torch.Tensor): The high resolution image
        spatial_offset (tuple): The spatial offset estimated by the 
            spatial_model_fit function.
    Returns:
        torch.Tensor: The transformed image
    """
    offset_image = spatial_model_transform_pixel(
        image1=lr_to_hr,
        spatial_offset=spatial_offset
    )
    hr_masked = hr * (offset_image != 0)
    
    # to numpy
    offset_image = offset_image.detach().cpu().numpy()
    hr_masked = hr_masked.detach().cpu().numpy()
    
    # Subpixel refinement
    from skimage.registration import phase_cross_correlation
    shift, error, diffphase = phase_cross_correlation(
        offset_image.mean(0), hr_masked.mean(0), upsample_factor=100
    )
    
    return spatial_model_transform_pixel(
        image1=torch.from_numpy(offset_image).float(),
        spatial_offset={"offset": list(np.int16(np.round(shift)))}
    )
    


model = spatial_setup_model()
matching_points = spatial_get_matching_points(
    img01=input_tensor_hat,
    img02=target_tensor_hat,
    model=model,
    spectral_reducer_method="mean",
    rgb_bands=[0, 1, 2],
)


spatial_offset = spatial_model_fit(
    matching_points=matching_points,
    n_points = 10,
    threshold_distance = 10**4,
    verbose = True,
)

spatial_offset["offset"] = [x*2 for x in spatial_offset["offset"]]
new_image = spatial_model_transform(
    lr_to_hr=input_tensor,
    hr=new_target_tensor,
    spatial_offset=spatial_offset
)

# save
tosave = "/home/gonzalo/Downloads/wetransfer_roi_1090__lm05_178032_19840630-tif_2023-10-06_1513/fixed.tif"
with rio.open(tosave, "w", **profile) as dst:
    dst.write(new_image*10000)


fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(input_tensor_hat[0:3].permute(1, 2, 0).numpy()*3)
ax[1].imshow(hr_masked[0:3].permute(1, 2, 0).numpy()*3)
ax[2].imshow(new_image[0:3].permute(1, 2, 0).numpy()*3)
plt.show()

