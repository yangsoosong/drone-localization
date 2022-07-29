import cv2

from .detection import detect_objects, load_model_cache, load_model_network


def test_load_model_network():
    load_model_network()

def test_load_model_cache():
    load_model_cache()

def test_detect_objects():
    image = cv2.imread('test.jpg')
    detect_objects(image)