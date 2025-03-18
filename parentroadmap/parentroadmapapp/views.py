from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Хочу стать родителем", 'url_name': 'prepregnancy'},
        {'title': "Ведение беременности", 'url_name': 'pregnancy'},
        {'title': "Я родитель", 'url_name': 'parenting'}
        ]

steps = [1, 2, 3, 4, 5]

def index(request):
    return render(request, 'parentroadmapapp/index.html',  {'title': 'Главная страница', 'menu': menu, 'steps': steps})


def prepregnancy(request):
    return render(request, 'parentroadmapapp/prepregnancy.html', {'title': 'Хочу стать родителем', 'menu': menu})


def pregnancy(request):
    return render(request, 'parentroadmapapp/pregnancy.html', {'title': 'Ведение беременности', 'menu': menu})


def parenting(request):
    return render(request, 'parentroadmapapp/parenting.html', {'title': 'Я родитель', 'menu': menu})
