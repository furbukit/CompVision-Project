import numpy as np
import cv2
import skimage


def rough_segmentation_mask(image, tminColor, tdiffColor):

    min_colors = np.min(image, axis=2)
    max_colors = np.max(image, axis=2)
    mask = np.where((min_colors < tminColor) | (max_colors - min_colors > tdiffColor), 1, 0) # Change 1 to 255 if you want to display
    
    return mask.astype(np.uint8)

def connected_component_analysis(image):
    # https://www.sciencedirect.com/science/article/pii/S0031320317301693
    label, labels = skimage.measure.label(image, background=0, return_num=True, connectivity=1)
    return (label.astype(np.uint8), labels)

def filter_clusters(image, min_area, max_area, axis_ratio):
    unique_values, value_counts = np.unique(image, return_counts=True)
    for value, count in zip(unique_values, value_counts):
        if count < min_area or count > max_area:
            image[image == value] = 0

    props = skimage.measure.regionprops(image)
    for prop in props:
        if prop.minor_axis_length == 0.0 or prop.major_axis_length == 0.0:
            image[image == prop.label] = -1
        elif (prop.minor_axis_length / prop.major_axis_length) > axis_ratio:
            print("here")
            image[image == prop.label] = -1

    return image.astype(np.uint8)

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
