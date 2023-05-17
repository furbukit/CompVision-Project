import numpy as np
import pandas as pd
import cv2
import skimage


def task1(image):
    # Performs CCA on the rough segmentation mask.
    
    return 0

def rough_mask(thresh1, thresh2, image):
    # Defines the rough segmentation mask.
    # Converts input image to a NumPy array.
    img = np.array(image)
    
    # Iterates through every pixel of image.
    mask_img = np.array()
    
    for row in img:
        img_row = np.array()
        for col in row:
            if np.min(col)<thresh1 or np.max(col)-np.min(col)>thresh2:
                img_row.append(col)
            else:
                img_row.append(0)
        mask_img.append(img_row)
    return mask_img
    


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