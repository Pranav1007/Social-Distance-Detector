import math
import numpy as np
from cv2 import cv2
from .config import WHT, CONF_THRESH, NMS_THRESH
from .config import RED, BLUE, GREEN, BLACK, WHITE
from .model import load_model

classNames, modelNet = load_model() 		# Load the yolo model


def calCentroid(xmn, ymn, xmx, ymx):
    """
        Function to calculate the centroid of a given image
    """
    xmid = (xmx + xmn) / 2
    ymid = (ymx + ymn) / 2
    return xmid, ymid


def get_distance(x1, x2, y1, y2):
    """
        Function to get the distance between any two points
    """
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


def main_func(img):
    """
        Function to obtain the outpur output from the yolo model
    """
    blob = cv2.dnn.blobFromImage(img, 1/255, (WHT, WHT), [0, 0, 0], crop=False)			# Yolo only accepts image of blob(Binary Large Object) format so we convert the image into blob format
    modelNet.setInput(blob)																# Setting the input image for the model
    layers = modelNet.getLayerNames()													# Obtain the names of all the layers of our network (Architecture)
    outputNames = [layers[i[0]-1] for i in modelNet.getUnconnectedOutLayers()]			# Get the names of only the output layers of the model
    outputs = modelNet.forward(outputNames)     										# Output layers of our Network
    return outputs


def findObjects(outputs, img):
    """
        Function to detect people and draw boxes around them based on whether they are social distancing or not, for the given media.
    """
    hT, wT, cT = img.shape		# Based on the image size we define the height and width.
    boundBox = [] 				# To keep track of all the bounding Boxes.
    classIds = []				# Class IDs of all the predictions (0 for person).
    confidenceVal = []		    # Confidence value of image detected (b/w 0 and 1).
    detectBox = []				# All the bounding boxes which we will have to print.
    centroids = []				# To keep track of the midpoint of the image detected.
    boxColours = []				# Based on the distance it will either be red or green.
    good = 0					# Number of people who are maintaining optimal distance.
    bad = 0						# Number of people who are not maintaining optimal distance.

    for output in outputs:
        for detection in output:
            scores = detection[5:] 	# First five classes include the dimensions of the image, we ignore them and only include the classID probavbilities
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > CONF_THRESH and classId == 0:
                # Width and Height
                w, h = int(detection[2] * wT), int(detection[3] * hT)
                x, y = int((detection[0] * wT) - w/2), int((detection[1] * hT) - h/2)
                boundBox.append([x, y, w, h]) 					# Append the dimensions of the image detected into the BoundBox Array
                classIds.append(classId)						# Append the classId of the image detected into the classId Array
                confidenceVal.append(float(confidence)) 		# Append the (predicted) confidence value of the image detected into the ConfidenceVal Array

    # Suppress all the overlapping, weak and redundant bounding boxes based on the confidence scores. This process is called Non-Maximum Suppression.
    indices = cv2.dnn.NMSBoxes(boundBox, confidenceVal, CONF_THRESH, NMS_THRESH)

    # We iterate over all the boundBoxes which after performing NMS
    for i in range(len(boundBox)):
        if i in indices:
            x, y, w, h = boundBox[i]								# Obtain the dimensions of the current Bound Box
            centroid = calCentroid(x, y, x + w, y + h) 				# Calculate and store the centroid value
            detectBox.append([x, y, x + w, y + h, centroid])		# Append the box dimensions to the detectBox matrix
            colour = 0					    						# Initialise colour flag to 0 (Person is safe by default)

            # We will now compare this image with all the other images detected and see if the person is at a safe distance
            for k in range(len(centroids)):
                c = centroids[k]
                # If the distance between two images(detected near each other) is less than 200 pixels.
                if(get_distance(c[0], centroid[0], c[1], centroid[1]) <= 200):
                    boxColours[k] = 1									# Since distance is less they are not social distancing
                    colour = 1											# Initialse colour flag to 1 (Red or Danger)
                    break									    		# We can break out as the person detected is dangerous.

            centroids.append(centroid)		# Append the centroid value to the centroid array.
            boxColours.append(colour)		# Append the colour value to the colour array. Later used while drawing Bound Box.

    # Drawing the Bound Boxes
    for i in range(len(detectBox)):
        box = detectBox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        if(boxColours[i] == 0):
            label = "SAFE"
            cv2.rectangle(img, (x, y), (w, h), GREEN, 2)										# Draw a Bound Box (Green)
            cv2.circle(img, (int(centroids[i][0]), int(centroids[i][1])), 4, GREEN, 2)          # Draw a circle at the centroid(Easier to identify the person)
            cv2.circle(img, (int(centroids[i][0]), int(centroids[i][1])), 8, GREEN, 2)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLACK, 2)			# Put the label based on the distance
            good += 1		                                                                    # Increment number of people who are safe
        else:
            label = "DANGER"
            cv2.rectangle(img, (x, y), (w, h), RED, 2)					        				# Draw a Bound Box (Red)
            cv2.circle(img, (int(centroids[i][0]), int(centroids[i][1])), 4, RED, 2)	        # Draw a circle at the centroid(Easier to identify the person)
            cv2.circle(img, (int(centroids[i][0]), int(centroids[i][1])), 8, RED, 2)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLACK, 2)			# Put the label based on the distance
            bad += 1		                                                                    # Increment number of people who are not safe

    # Printing details of the image on the top left corner.
    text = f'Number of persons identified: {str(bad + good)}'
    text_bad = f'Number of persons not practicing social distancing: {str(bad)} '
    text_good = f'Number of persons practicing social distancing: {str(good)}'
    text_conf = f'Confidence Threshold: {str(CONF_THRESH * 100)}%'
    text_nms = f'Non-Maximum Suppression Threshold: {str(NMS_THRESH * 100)}%'

    cv2.rectangle(img, (15, 5), (485, 105), WHITE, cv2.FILLED)
    cv2.putText(img, text_conf, (40, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLUE, 2)
    cv2.putText(img, text_nms, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLUE, 2)
    cv2.putText(img, text, (40, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, BLACK, 2)
    cv2.putText(img, text_good, (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN, 2)
    cv2.putText(img, text_bad, (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)
