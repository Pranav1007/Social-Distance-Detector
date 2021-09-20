import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Base Path for the YOLO Directory
MODEL_PATH = os.path.join(ROOT_DIR, "yolo/model")
CLASSES_PATH = os.path.join(ROOT_DIR, "yolo")

# Confidence Threshold Value. If it is greater than 50% we will save whatever the model detects.
CONF_THRESH = 0.5

# Non-Maxima Suppression Threshold. It helps in eliminating the overlapping boxes. (Suppressing all the non maximum boxes)
# If the threshold is very high, lesser boxes will be removed
# If the threshold is very low, almost all the boxes will be removed
NMS_THRESH = 0.3

# Pixel Distance to categorise people into two groups: those who are socially distanced and those who are not
DIS_THRESH = 120

# Width and Height in Pixels
WHT = 416

# OpenCV Colour Codes
RED = (0, 0, 255)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# True if GPU is used for computation
USE_GPU = False
