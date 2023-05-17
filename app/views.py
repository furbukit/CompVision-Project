# This file defines the app's views. 
# A view is a Python function that takes a request object and returns an HTTP response. 
# You can use this file to define the logic for handling HTTP requests and returning HTTP responses.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest, FileResponse
from .image_analysis.analyze import task1, task2, task3
from .utils import create_nested_dropdown_options, base64_image, process_image
import cv2
import os
from django.templatetags.static import static
from django.conf import settings
import base64
import numpy as np

# Create your views here.
def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def hello(request):
    return HttpResponse("Hello, world!")



def dropdown_data(request):
    # Fetch the file information from your desired folder or data source
    data_folder = os.path.abspath('app/data') # Replace with the actual path to your data folder

    file_data = []  # List to store the file information

    # Iterate over the subfolders in the data folder
    for group in os.listdir(data_folder):
        if group != "camera parameters":
            group_path = os.path.join(data_folder, group)

            # Check if the item is a subfolder
            if os.path.isdir(group_path):
                # Iterate over the files in the subfolder
                for file_name in os.listdir(group_path):
                    file_path = os.path.join(group_path, file_name)

                    # Check if the item is a file
                    if os.path.isfile(file_path):
                        # Append the file information to the list
                        file_data.append({
                            'group': group,
                            'name': file_name,
                            'path': file_path,
                        })
        else:
            continue

    # Create a JSON response with the file data
    return JsonResponse(file_data, safe=False)

def get_image(request):
    print(request)
    image_path = request.GET.get('path')
    edited = request.GET.get('edit')
    if image_path == "" or image_path is None or image_path == " ":
        response = HttpResponse("Image not found")
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response
    
    image_file_path = os.path.abspath('app/data/' + image_path)
    print(image_file_path)
    print(f"EDITED: {edited}")
    if edited == 'f':
        response = FileResponse(open(image_file_path, 'rb'), content_type='image/png')
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response
    elif edited == 't':
        response = FileResponse(open(image_file_path, 'rb'), content_type='image/png')
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response

    else:
        response = HttpResponse("Image not found")
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response
"""
def task_one(request):
    print("WE GOT HERE")
    path = os.path.abspath('app/static/data')
    dropdown_options = create_nested_dropdown_options(path)

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        selected_image_path = request.POST.get('selected_image_path')
        img_base64_original, img_base64_edited = process_image(selected_image_path)
    else:
        img_base64_original, img_base64_edited = process_image()
    
    context = {
        'dropdown_options': dropdown_options,
        'img_base64_edited': img_base64_edited,
        'img_base64_original': img_base64_original,
    }
    print(img_base64_edited[-10:])
    return render(request, 'pages/task_one.html', context)

def task_two(request):
    image_path = os.path.abspath('app/static/data/camera 11/2022_12_15_15_51_19_927_rgb_left.png')
    # Load the image as a NumPy array
    img = cv2.imread(image_path)

    processed_img = task2(img)

    # PROCESSED IMG SHOULD BE A NUMPY ARRAY HERE

    _, buffer = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    context = {'img_base64': img_base64}
    return render(request, 'pages/task_two.html', context)

def task_three(request):
    image_path = os.path.abspath('app/static/data/camera 11/2022_12_15_15_51_19_927_rgb_left.png')
    # Load the image as a NumPy array
    img = cv2.imread(image_path)

    processed_img = task3(img)

    # PROCESSED IMG SHOULD BE A NUMPY ARRAY HERE

    _, buffer = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    context = {'img_base64': img_base64}
    return render(request, 'pages/task_three.html', context)
"""