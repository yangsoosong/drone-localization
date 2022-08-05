"""
Functions for working with YOLOv5 to detect objects in images.
"""
from pathlib import Path
from urllib.error import URLError

import cv2
import torch
from socket import gaierror

# Model
def load_model_network():
    """Load YOLOv5 model."""
    try:
        return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).eval()
    except (gaierror, URLError):
        return None

def load_model_cache():
    """Load locally stored YOLOv5 model."""
    try:
        path = Path.home() / '.cache/torch/hub/ultralytics_yolov5_master'
        return torch.hub.load(str(path), 'yolov5s', source='local', pretrained=True).eval()
    except:
        print("You must run `tello download` while connected to network first!")
        return None

def detect_objects(image):
    """Apply YOLOv5 to an image to detect objects
    Parameters
    ----------
    image : numpy array

    Returns
    -------
    image : numpy array
        The parameter image, with bounding boxes around each object detected
    detections : pandas dataframe
        A table of the objects detected in the picture with boundaries,
        confidence, and identification values for each object.
    """
    model = load_model_cache()
    if model is None:
        print('Detection model not found!')
        return image, []
    detections = model([image]).pandas().xyxy[0]
    # print('detections', detections)
    for label, confidence, left, right, bottom, top in detections[['name', 'confidence', 'xmin', 'xmax', 'ymin', 'ymax']].values:
        cv2.rectangle(image, (round(left), round(top)), (round(right), round(bottom)), (255, 0, 0), 2)
        cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                            (round(left), round(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 0, 255), 1)
    return image, detections
