from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print(request)
    return HttpResponse('Hello World!!!')

def test(request):
    print(request)
    return HttpResponse('Hello World!!!')
