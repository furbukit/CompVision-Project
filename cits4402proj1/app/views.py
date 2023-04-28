# This file defines the app's views. 
# A view is a Python function that takes a request object and returns an HTTP response. 
# You can use this file to define the logic for handling HTTP requests and returning HTTP responses.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def hello(request):
    return HttpResponse("Hello, world!")

def task_one(request):
    return render(request, 'pages/task_one.html')

def task_two(request):
    return render(request, 'pages/task_two.html')

def task_three(request):
    return render(request, 'pages/task_three.html')

