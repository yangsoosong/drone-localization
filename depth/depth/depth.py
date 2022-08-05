"""
Functions for working with MiDaS to detect depth in images.
"""

import urllib.request
from pathlib import Path

import cv2
import torch
import matplotlib.pyplot as plt

model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

def load_model_network():
    """
    Load the PyTorch Hub MiDaS model set to evaluation mode. Use graphics
    card if available. If not, use CPU.
    """
    try:
        midas = torch.hub.load("intel-isl/MiDaS", model_type)
        device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        midas.to(device)
        midas.eval()
        return midas
    except Exception as e:
        print(e)
        return None

def load_model_cache():
    """Load a MiDaS model that has been stored locally."""

    try:
        path = Path.home() / '.cache/torch/hub/intel-isl_MiDaS_master'
        midas = torch.hub.load(str(path), model_type, source='local').eval()
        device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        midas.to(device)
        midas.eval()
        return midas
    except:
        print("You must run `tello download` while connected to network first!")
        return None

def load_transforms_network():
    """Load MiDaS transforms."""

    try:
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

        if model_type in ["DPT_Large", "DPT_Hybrid"]:
            transform = midas_transforms.dpt_transform
        else:
            transform = midas_transforms.small_transform

        return transform
    except Exception as e:
        print(e)
        return None

def load_transforms_cache():
    """Load locally stored MiDaS transforms"""
    try:
        path = Path.home() / '.cache/torch/hub/intel-isl_MiDaS_master'
        midas_transforms = torch.hub.load(str(path), "transforms", source='local')

        if model_type in ["DPT_Large", "DPT_Hybrid"]:
            transform = midas_transforms.dpt_transform
        else:
            transform = midas_transforms.small_transform

        return transform
    except Exception as e:
        print(e)
        return None

def load_img():
    """Return a cv2 render of a test image."""

    url, filename = ("https://github.com/intel-isl/MiDaS/releases/download/v2/dog.jpg", "dog.jpg")
    urllib.request.urlretrieve(url, filename)
    return cv2.imread('dog.jpg')

def detect_depth(img):
    """ Return a prediction of depth in img."""

    model = load_model_cache()
    transform = load_transforms_cache()

    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    input_batch = transform(img).to(device)

    with torch.no_grad():
        prediction = model(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    return prediction.cpu().numpy()

def visualize_prediction(img, prediction):
    """
    Function to produce a visualization of the application of the supplied model
    (prediction) to the supplied image (img).

    Parameters
    ----------
    img : numpy array
        Numpy array representation of an image.
    prediction : numpy array
        Representation of the depth model applied to the image. Output of detect_depth().
    """
    prediction = cv2.resize(prediction, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
    depth_min = prediction.min()
    depth_max = prediction.max()
    img_out = (255 * (prediction - depth_min) / (depth_max - depth_min)).astype("uint8")

    plt.imshow(img_out)
    plt.show()
