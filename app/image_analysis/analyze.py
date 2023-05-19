import numpy as np
import pandas as pd
import cv2
import skimage
import os
from .utils import rough_segmentation_mask, connected_component_analysis, filter_clusters

path = os.path.abspath('app/data')

def task1(image, upper, lower, area_upper, area_lower, axis_ratio):
    # Performs CCA on the rough segmentation mask.
    # convert the image to OpenCV format
    print(upper, lower, area_upper, area_lower, axis_ratio)
    cv_image = cv2.imread(image)
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    mask_img = rough_segmentation_mask(rgb_image, upper, lower)
    connected_components, labels = connected_component_analysis(mask_img)
    print(np.max(connected_components), np.min(connected_components))
    print(f"labels {labels}")
    # Right up till here
    image_out, props, nearest_clusters = filter_clusters(connected_components, area_lower, area_upper, axis_ratio)

    return image_out.astype(np.uint8)


def task2(image):
    # convert the image to OpenCV format
    cv_image = image

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (0, 255, 0), 2)

    # return the analyzed image as a NumPy array
    return cv_image

def task3(image):
    # convert the image to OpenCV format
    cv_image = image

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (0, 0, 255), 2)

    # return the analyzed image as a NumPy array
    return cv_image