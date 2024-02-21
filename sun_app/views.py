from django.shortcuts import render
from django.http import HttpResponse

def sun_app(request):
    return HttpResponse("Hello world!")
# Create your views here.
def bun_app(request):
    return HttpResponse("Hello Bun!")