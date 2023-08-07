from django.shortcuts import render, HttpResponse

# Create your views here.

# This is where the views/webpage information for the end user goes into 

def say_hello(request):
    return HttpResponse("Hello")