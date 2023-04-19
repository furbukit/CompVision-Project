# This file defines the app's views. 
# A view is a Python function that takes a request object and returns an HTTP response. 
# You can use this file to define the logic for handling HTTP requests and returning HTTP responses.
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world!")
# Create your views here.
