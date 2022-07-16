import torch
import cv2
from pathlib import Path

# Model
try:
    print('Loading model...')
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).eval()
except Exception as e:
    print(e)
    print('Offline mode')
    try:
        model = torch.hub.load(Path(Path.home(), Path('.cache/torch/hub/ultralytics_yolov5_master')), 'yolov5s', source='local', pretrained=True).eval()
    except Exception as e:
        print(e)
        raise Exception("You need to run the script at least once online to make sure you have the model downloaded.")

def detect_objects(image):
    detections = model([image]).pandas().xyxy[0]
    print('detections', detections)
    for label, confidence, left, right, bottom, top in detections[['name', 'confidence', 'xmin', 'xmax', 'ymin', 'ymax']].values:
        print(f'label: {label}')
        print(f'confidence: {confidence}')
        print(f'left: {left}')
        print(f'top: {top}')
        print(f'right: {right}')
        print(f'bottom: {bottom}')
        cv2.rectangle(image, (round(left), round(top)), (round(right), round(bottom)), (255, 0, 0), 2)
        cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                            (round(left), round(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 0, 255), 1)
    return image, detections