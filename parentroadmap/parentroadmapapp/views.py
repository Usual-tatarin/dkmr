from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)