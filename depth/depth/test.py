import cv2

from .depth import (detect_depth, load_model_cache, load_model_network,
                    visualize_prediction)


def test_load_model_network():
    load_model_network()

def test_load_model_cache():
    load_model_cache()

def test_detect_objects():
    image = cv2.imread('test.jpg')
    detect_depth(image)

def test_visualize_prediction():
    image = cv2.imread('test.jpg')
    prediction = detect_depth(image)
    visualize_prediction(image, prediction)