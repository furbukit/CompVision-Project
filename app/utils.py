import os
import cv2
import base64
import tempfile
import numpy as np
path = os.path.abspath('app/data')

def create_nested_dropdown_options(path):
    """
    Recursively create nested HTML <select> tags for the given path.
    """
    options = ""
    if os.path.isdir(path):
        # Get the directory name and add it as a top-level option
        dirname = os.path.basename(path)

        # Recursively generate options for each subdirectory
        for name in os.listdir(path):
            subpath = os.path.join(path, name)
            if os.path.isdir(subpath) and name != "camera_parameters":
                options += '<optgroup label="' + name + '">' + create_nested_dropdown_options(subpath) + "</optgroup>"
            elif os.path.isfile(subpath) and name.endswith(".png"):
                img_path = os.path.join(dirname, name)
                options += f'<option value="{img_path}">{name}</option>'

    return options

def process_image(selected_image_path='camera 11/2022_12_15_15_51_19_927_rgb_left.png'):
    print(selected_image_path)
    image_path = os.path.abspath(path+"/"+selected_image_path)
    img = cv2.imread(image_path)
    img_base64_original = base64_image(img)

    processed_img = img
    img_base64_edited = base64_image(processed_img)

    print(np.mean(img))
    print(np.mean(processed_img))
    return img_base64_original, img_base64_edited

def base64_image(img):
    print(img)
    _, buffer = cv2.imencode('.png', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return img_base64