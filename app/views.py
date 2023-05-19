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
import io
from PIL import Image

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
        upper = int(request.GET.get('segupper'))
        lower = int(request.GET.get("seglower"))
        area_upper = int(request.GET.get('areaupper'))
        area_lower = int(request.GET.get('arealower'))
        axis_ratio = float(request.GET.get('axisratio'))
        task = int(request.GET.get('task'))
        if (task == 1):
            out_fin, props, nearest_clusters = task1(image_file_path, upper, lower, area_upper, area_lower, axis_ratio)
        if (task == 2):
            out_fin = task2(image_file_path, upper, lower, area_upper, area_lower, axis_ratio, gain=1.1)
        if (task == 3):
            out1 = task1(image_file_path, upper, lower, area_upper, area_lower, axis_ratio)
            out2 = task2(out1)
            out_fin = task3(out2)
        
        pil_image = Image.fromarray(out_fin.astype(np.uint8))
        image_stream = io.BytesIO()
        pil_image.save(image_stream, format='PNG')
        image_stream.seek(0)
        response = FileResponse(image_stream, content_type='image/png')
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response

    else:
        response = HttpResponse("Image not found")
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response
