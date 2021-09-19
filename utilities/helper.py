from cv2 import cv2
import math
from .functions import main_func, findObjects, load_model

classNames, modelNet = load_model()


def image(path):
    img = cv2.imread(path)
    outputs = main_func(img)
    findObjects(outputs, img)
    cv2.imshow("Detection Output", img)
    cv2.waitKey(0)


def video(path):
    cap = cv2.VideoCapture(path)
    while True:
        success, img = cap.read()
        if success:
            outputs = main_func(img)
            findObjects(outputs, img)
            cv2.imshow("Detection Output", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error Loading Media. Please try again")


def webcam():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if success:
            outputs = main_func(img)
            findObjects(outputs, img)
            cv2.imshow("Detection Output", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Video Camera Error. Please try again later.")
