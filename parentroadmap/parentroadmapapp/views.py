from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

menu = [{'title': "Хочу стать родителем", 'url_name': 'prepregnancy'},
        {'title': "Ведение беременности", 'url_name': 'pregnancy'},
        {'title': "Я родитель", 'url_name': 'parenting'}
]

def index(request):
    return render(request, 'parentroadmapapp/index.html', {'title': 'Главная страница', 'menu': menu})

def prepregnancy(request):
    return render(request, 'parentroadmapapp/prepregnancy.html', {'title': '{Хочу стать родителем}'})

def pregnancy(request):
    return render(request, 'parentroadmapapp/pregnancy.html', {'title': 'Ведение беременности'})

def parenting(request):
    return render(request, 'parentroadmapapp/parenting.html', {'title': 'Я родитель'})