from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def my_app_view(request):
    return HttpResponse("Hello, this is my app view!")