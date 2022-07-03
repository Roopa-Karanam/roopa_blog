# mysite/views.py

from django.http import HttpResponse
from django.shortcuts import render
from roopa_blog import views


def index(request):
    return HttpResponse('Hello world!')

