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
    # Right up till here
    out = filter_clusters(connected_components, area_lower, area_upper, axis_ratio)
    print(out)
    out = np.where(out != 0, 255, out)


    return out


def task2(cv_image, gain):
    # convert the image to OpenCV format
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    # Calculates the mean for each colour
    mean_red = int(np.mean(rgb_image[:, 0]))
    mean_green = int(np.mean(rgb_image[:, 1]))
    mean_blue = int(np.mean(rgb_image[:, 2]))

    compensation = (gain * mean_red, gain * mean_green, gain * mean_blue)
    
    # if max(compensation) == compensation[0]:
    #     #cluster is red
    #     return None
    
    # elif max(compensation) == compensation[1]:
    #     #cluster be blue
    #     return None
    
    # elif max(compensation) == compensation[2]:
    #     #cluster be green
    #     return None
    
    cluster_clr = None

    for colour in compensation:
        if max(compensation) == colour:
            cluster_clr = colour

    
    




# Calculate mean color for each cluster
    for i, cluster in enumerate(clusters):
        mean_color = compute_mean_color(cluster)
        print(f"Mean color for cluster {i+1}: {mean_color}")
    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image

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