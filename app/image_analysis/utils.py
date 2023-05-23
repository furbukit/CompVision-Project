import numpy as np
import cv2
import skimage
from scipy.spatial.distance import cdist

def rough_segmentation_mask(image, tminColor, tdiffColor):

    min_colors = np.min(image, axis=2)
    max_colors = np.max(image, axis=2)
    mask = np.where((min_colors < tminColor) | (max_colors - min_colors > tdiffColor), 255, 0) # Change 1 to 255 if you want to display
    
    return mask

def connected_component_analysis(image):
    # https://www.sciencedirect.com/science/article/pii/S0031320317301693
    label, labels = skimage.measure.label(image, background=0, return_num=True, connectivity=1)
    return (label, labels)

def filter_clusters(labels, min_area, max_area, axis_ratio):
    # Filter objects clusters by area
    unique_values, value_counts = np.unique(labels, return_counts=True)
    for value, count in zip(unique_values, value_counts):
        if count < min_area or count > max_area:
            labels[labels == value] = 0

    props = skimage.measure.regionprops(labels)

    # Remove all non-round clusters
    for prop in props:
        #print(prop.minor_axis_length, prop.major_axis_length, prop.label, round(prop.minor_axis_length/prop.major_axis_length, 2))
        if (prop.minor_axis_length / prop.major_axis_length) < axis_ratio:
            labels[labels == prop.label] = 0

    props = skimage.measure.regionprops(labels)
    print(f"PROPS: {type(props)}     {props}")
    centroids = np.array([prop.centroid for prop in props])
    print(f"PROPS: {type(centroids)}     {centroids}")
    # Calculate pairwise distances between centroids
    distances = cdist(centroids, centroids)
    
    # Find the 5 nearest clusters for each cluster
    nearest_clusters = []
    for i in range(len(centroids)):
        nearest_indices = np.argsort(distances[i])[1:6]  # Exclude the current cluster itself??? [1:6]
        nearest_clusters.append(nearest_indices)
    # Draw centroids and ellipses on the image
    image_rgb = cv2.cvtColor(labels.astype(np.uint8), cv2.COLOR_GRAY2RGB)

    for i, prop in enumerate(props):
        centroid = prop.centroid

        points = np.array([centroids[j] for j in nearest_clusters[i]])
        points = np.array([[point[1], point[0]] for point in points])
        # Get the points for ellipse fitting
        ellipse = cv2.fitEllipse(points.astype(int))
        semi_major_axis = max(ellipse[1][0], ellipse[1][1]) / 2.0
        semi_minor_axis = min(ellipse[1][0], ellipse[1][1]) / 2.0
        area = np.pi * semi_major_axis * semi_minor_axis

        cv2.circle(image_rgb, (int(centroid[1]), int(centroid[0])), 5, (255, 0, 0), -1)  # Draw centroid as blue circle
        if (ellipse[1][0] != float(0)):
            if ((ellipse[1][1]/ellipse[1][0]) > 1.6) or (area > 4000):
                continue
            else:
                cv2.ellipse(image_rgb, ellipse, (0, 255, 0), 2)  # Draw ellipse as green contour

    return (image_rgb, props, nearest_clusters)
