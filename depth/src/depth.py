import cv2
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub

def load_model_network():
    try:
        return hub.load("https://tfhub.dev/intel/midas/v2/2", tags=['serve'])
    except Exception as e:
        print(e)
        return None

def load_model_cache():
    try:
        path = Path.home() / '.cache/torch/hub/intel_midas_v2_2'
        return hub.load(str(path), tags=['serve'])
    except Exception as e:
        print(e)
        return None

def load_img():
    url, filename = ("https://github.com/intel-isl/MiDaS/releases/download/v2/dog.jpg", "dog.jpg")
    urllib.request.urlretrieve(url, filename)
    return cv2.imread('dog.jpg')

def detect_depth(img):
    model = load_model_cache()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0
    img_resized = tf.image.resize(img, [384,384], method='bicubic', preserve_aspect_ratio=False)
    img_resized = tf.transpose(img_resized, [2, 0, 1])
    img_input = img_resized.numpy()
    reshape_img = img_input.reshape(1,3,384,384)
    tensor = tf.convert_to_tensor(reshape_img, dtype=tf.float32)

    output = model.signatures['serving_default'](tensor)
    prediction = output['default'].numpy()
    prediction = prediction.reshape(384, 384)

    return prediction

def visualize_prediction(img, prediction):
    prediction = cv2.resize(prediction, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
    depth_min = prediction.min()
    depth_max = prediction.max()
    img_out = (255 * (prediction - depth_min) / (depth_max - depth_min)).astype("uint8")

    plt.imshow(img_out)
    plt.show()
