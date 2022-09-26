from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text = '<h1> Hi how are you guys</h1>'
    return HttpResponse(text)