from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    text = """<h1> this is first app </h1>
    <h1> this is first app </h1>
    <h1> this is first app </h1>
    <h1> this is first app </h1>"""
    return HttpResponse(text)