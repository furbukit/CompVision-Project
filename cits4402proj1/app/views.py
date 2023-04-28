# This file defines the app's views. 
# A view is a Python function that takes a request object and returns an HTTP response. 
# You can use this file to define the logic for handling HTTP requests and returning HTTP responses.
from django.shortcuts import render
from django.http import HttpResponse
from .image_analysis.analyze import task1, task2, task3
import cv2
import os
from django.templatetags.static import static
from django.conf import settings
import base64

# Create your views here.
image_path = os.path.abspath('app/static/data/camera 11/2022_12_15_15_51_19_927_rgb_left.png')

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def hello(request):
    return HttpResponse("Hello, world!")

def task_one(request):
    # Load the image as a NumPy array
    img = cv2.imread(image_path)

    processed_img = task1(img)

    # PROCESSED IMG SHOULD BE A NUMPY ARRAY HERE

    _, buffer = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    context = {'img_base64': img_base64}
    return render(request, 'pages/task_one.html', context)

def task_two(request):
    # Load the image as a NumPy array
    img = cv2.imread(image_path)

    processed_img = task2(img)

    # PROCESSED IMG SHOULD BE A NUMPY ARRAY HERE

    _, buffer = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    context = {'img_base64': img_base64}
    return render(request, 'pages/task_two.html', context)

def task_three(request):
    # Load the image as a NumPy array
    img = cv2.imread(image_path)

    processed_img = task3(img)

    # PROCESSED IMG SHOULD BE A NUMPY ARRAY HERE

    _, buffer = cv2.imencode('.png', processed_img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    context = {'img_base64': img_base64}
    return render(request, 'pages/task_three.html', context)
