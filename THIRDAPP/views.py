from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wow(request):
    return HttpResponse("this is my third app")
