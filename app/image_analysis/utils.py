import numpy as np
import cv2
import skimage
from scipy.spatial.distance import cdist

def rough_segmentation_mask(image, tminColor, tdiffColor):

    min_colors = np.min(image, axis=2)
    max_colors = np.max(image, axis=2)
    mask = np.where((min_colors < tminColor) | (max_colors - min_colors > tdiffColor), 255, 0) # Change 1 to 255 if you want to display
    
    return mask.astype(np.uint8)

def connected_component_analysis(image):
    # https://www.sciencedirect.com/science/article/pii/S0031320317301693
    label, labels = skimage.measure.label(image, background=0, return_num=True, connectivity=1)
    return (label, labels)

def filter_clusters(labels, min_area, max_area, axis_ratio):
    # Filter objects clusters by area
    unique_values, value_counts = np.unique(labels, return_counts=True)
    print(f"value counts {len(unique_values)}")
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
    centroids = np.array([prop.centroid for prop in props])

    # Calculate pairwise distances between centroids
    distances = cdist(centroids, centroids)
    
    # Find the 5 nearest clusters for each cluster
    nearest_clusters = []
    thresh = 37
    for i in range(len(centroids)):
        nearest_indices = np.argsort(distances[i])[1:6]  # Exclude the current cluster itself??? [1:6]
        if(max(np.argsort(distances[i])[1:6])) > thresh:
            nearest_clusters.append(np.array([-1, -1, -1, -1, -1])) # If there is less than 6 clusters within thresh
        else:
            nearest_clusters.append(nearest_indices)
        print(nearest_clusters[i])
    print(nearest_clusters)
    # Draw centroids and ellipses on the image
    image_rgb = cv2.cvtColor(labels.astype(np.uint8), cv2.COLOR_GRAY2RGB)

    props = skimage.measure.regionprops(image_rgb)

    for i, prop in enumerate(props):
        centroid = prop.centroid

        print(prop.label, i, nearest_clusters[i], centroid)

        # If the cluster 
        if -1 not in nearest_clusters[i]:
            points = np.array([centroids[j] for j in nearest_clusters[i]])
            points = np.array([[point[1], point[0]] for point in points])
            print(points)
            # Get the points for ellipse fitting
            ellipse = cv2.fitEllipse(points.astype(int))

            cv2.circle(image_rgb, (int(centroid[1]), int(centroid[0])), 5, (255, 0, 0), -1)  # Draw centroid as blue circle
            cv2.ellipse(image_rgb, ellipse, (0, 255, 0), 2)  # Draw ellipse as green contour

    return (image_rgb, props, nearest_clusters)

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
