from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Хочу стать родителем", 'url_name': 'prepregnancy'},
        {'title': "Ведение беременности", 'url_name': 'pregnancy'},
        {'title': "Я родитель", 'url_name': 'parenting'}
        ]


def index(request):
    return render(request, 'webApp/index.html', {'title': 'Главная страница', 'menu': menu})


def prepregnancy(request):
    return render(request, 'webApp/prepregnancy.html', {'title': 'Хочу стать родителем', 'menu': menu})


def pregnancy(request):
    return render(request, 'webApp/pregnancy.html', {'title': 'Ведение беременности', 'menu': menu})


def parenting(request):
    return render(request, 'webApp/parenting.html', {'title': 'Я родитель', 'menu': menu})
