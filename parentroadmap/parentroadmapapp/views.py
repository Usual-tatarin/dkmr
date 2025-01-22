from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
def index(request):
    return render(request, 'parentroadmapapp/index.html', {'title': 'Главная страница'})
