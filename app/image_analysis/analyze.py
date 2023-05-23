import numpy as np
import pandas as pd
import cv2
import skimage
import math
import os
from .utils import rough_segmentation_mask, connected_component_analysis, filter_clusters
from skimage.measure import regionprops

path = os.path.abspath('app/data')

def task1(image, tmin, tdiff, area_upper, area_lower, axis_ratio):
    # Performs CCA on the rough segmentation mask.
    # convert the image to OpenCV format
    cv_image = cv2.imread(image)
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    mask_img = rough_segmentation_mask(rgb_image, tmin, tdiff)
    connected_components, labels = connected_component_analysis(mask_img)
    conny_components = np.copy(connected_components)
    # Right up till here
    image_out, props, nearest_clusters = filter_clusters(conny_components, area_lower, area_upper, axis_ratio)

    return image_out, props, nearest_clusters


def task2(image, upper, lower, area_upper, area_lower, axis_ratio, gain=1):
    # image out should already be a NumPy array
    image_out, props, nearest_clusters = task1(image, upper, lower, area_upper, area_lower, axis_ratio)
    cv_image = cv2.imread(image)
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    rgb_image = np.clip(rgb_image * gain, 0, 255)

    hex_sets = set()
    for i, prop in enumerate(props):
        centroid = prop.centroid
        hexagon = np.append(nearest_clusters[i], [i])
        hexagon = tuple(np.sort(hexagon))
        hex_sets.add(hexagon)

    new_clusters = []
    centroids = np.array([prop.centroid for prop in props])

    # Remove non-viable hexagons and convert to NumPy array
    for i, clust in enumerate(nearest_clusters):
        points = np.array([centroids[j] for j in clust])
        points = np.array([[point[1], point[0]] for point in points])

        # Get the points for ellipse fitting
        ellipse = cv2.fitEllipse(points.astype(int))

        if (ellipse[1][1] / ellipse[1][0]) > 1.7:
            new_clusters.append(np.array([-1, -1, -1, -1, -1]))
        else:
            new_clusters.append(np.array(clust))
    new_clusters = np.array(new_clusters)

    hex_sets = set()
    for i, prop in enumerate(props):
        hexagon = np.append(new_clusters[i], [i])
        hexagon = tuple(np.sort(hexagon))
        hex_sets.add(hexagon)
    hex_arr = np.array(list(hex_sets))

    # Sort order of dots
    new_hex_arr = []
    for hexagon in hex_arr:
        angles = []
        centroid = np.mean([props[label].centroid for label in hexagon], axis=0)
        for label in hexagon:
            points = np.array([centroids[j] for j in hexagon])
            points = np.array([[point[1], point[0]] for point in points])

            centroid_row = int(props[label].centroid[0])
            centroid_col = int(props[label].centroid[1])

            # Plot dot in center of target
            angle = math.atan2(centroid_row - centroid[0], centroid_col - centroid[1])
            angles.append(angle)
        
        hexagon = [label for _, label in sorted(zip(angles, hexagon), key=lambda x: x[0])]
        print(hexagon)
        hexagon2 = hexagon[1:] + [hexagon[0]]
        new_hex_arr.append(hexagon2)

    print(new_hex_arr)

    count = 0
    # Plot bounding rectangles for each cluster in hex_arr
    for hexagon in new_hex_arr:
        if(hexagon[0] != -1):
            print(hexagon)
            color_string = ""
            miniest_row = np.inf
            miniest_col = np.inf
            for label in hexagon:
            #     for attr in dir(props[label]):
            #         if not attr.startswith('__'):  # Exclude special attributes
            #             value = getattr(props[label], attr)
            #             print(f'{attr}: {value}')
                print(props[label].bbox[0], props[label].bbox[1], props[label].bbox[2], props[label].bbox[3])
                min_row = props[label].bbox[0]
                min_col = props[label].bbox[1]
                max_row = props[label].bbox[2]
                max_col = props[label].bbox[3]
                miniest_row = min(miniest_row, min_row)
                miniest_col = min(miniest_col, min_col)
                points = np.array([centroids[j] for j in hexagon])
                points = np.array([[point[1], point[0]] for point in points])

                # Get the points for ellipse fitting
                ellipse = cv2.fitEllipse(points.astype(int))

                # Plot rectangle surround target
                cv2.rectangle(rgb_image, (min_col, min_row), (max_col, max_row), (255, 0, 0), 2)
                # Plot dot on every target
                centroid_row = int(props[label].centroid[0])
                centroid_col = int(props[label].centroid[1])
                
                # Plot dot in centre of target
                ellipse_center = ellipse[0]
                center_row = int(ellipse_center[1])
                center_col = int(ellipse_center[0])
                
                cv2.circle(rgb_image, (center_col, center_row), 3, (255, 0, 0), -1)
                pixel_color = rgb_image[centroid_row, centroid_col]
                if max(pixel_color) == pixel_color[0]:
                    color_string += 'R'
                elif max(pixel_color) == pixel_color[1]:
                    color_string += 'G'
                else:
                    color_string += 'B'
                count +=1
                cv2.circle(rgb_image, (centroid_col, centroid_row), 3, (255, 255, 255), -1)

            text = f'{color_string}_{count//6}'
            text_org = (miniest_col, miniest_row - 20)  # Position of the text
            font_face = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.8
            text_color = (255, 0, 0)  # Red color for the text
            text_thickness = 2
            cv2.putText(rgb_image, text, text_org, font_face, font_scale, text_color, text_thickness)

    unique, counts = np.unique(image_out, return_counts=True)
    print(unique, counts)
    return rgb_image

def task3(image):
    # convert the image to OpenCV format
    cv_image = image

    # perform some analysis on the image using cv2
    # for example, draw a rectangle on the image
    cv2.rectangle(cv_image, (50, 50), (200, 200), (0, 0, 255), 2)

    # return the analyzed image as a NumPy array
    return cv_image