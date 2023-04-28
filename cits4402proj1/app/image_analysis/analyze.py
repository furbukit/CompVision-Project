import numpy as np
import pandas as pd
import cv2


def task1(image):
    # convert the image to OpenCV format
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (255, 0, 0), 2)

    # return the analyzed image as a NumPy array
    return cv_image

def task2(image):
    # convert the image to OpenCV format
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (0, 255, 0), 2)

    # return the analyzed image as a NumPy array
    return cv_image

def task3(image):
    # convert the image to OpenCV format
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (0, 0, 255), 2)

    # return the analyzed image as a NumPy array
    return cv_image