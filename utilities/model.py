import os
from cv2 import cv2
from .config import MODEL_PATH, CLASSES_PATH, USE_GPU

modelConfig = os.path.join(MODEL_PATH, "yolov3.cfg")
modelWeights = os.path.join(MODEL_PATH, "yolov3.weights")
modelClass = os.path.join(CLASSES_PATH, "coco.names")

backend = cv2.dnn.DNN_BACKEND_OPENCV
target = cv2.dnn.DNN_TARGET_CPU

if USE_GPU:
    backend = cv2.dnn.DNN_TARGET_CUDA
    target = cv2.dnn.DNN_TARGET_CUDA


def load_model():
    """
        Function to load the yolo model and class names
    """
    with open(modelClass, 'rt') as f:
        classNames = f.read().strip('\n')

    modelNet = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)    # Loading the YOLO Object Detector Model
    modelNet.setPreferableBackend(backend)   	                        # Setting OpenCV as our preferable backend
    modelNet.setPreferableTarget(target)     		                # Setting Target as CPU

    return classNames, modelNet
