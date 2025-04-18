from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Хочу стать родителем", 'url_name': 'prepregnancy'},
        {'title': "Ведение беременности", 'url_name': 'pregnancy'},
        {'title': "Я родитель", 'url_name': 'parenting'}
        ]

menu_items = [
    {'title': 'Очень длинный текст, который не помещается в одну строку', 'url': '/'},
    {'title': 'О нас', 'url': '/about/'},
    {'title': 'Контакты', 'url': '/contacts/'},
    {'title': 'Блог', 'url': '/blog/'},
]

def index(request):
    return render(request, 'parentroadmapapp/index.html',  {'title': 'Главная страница', 'menu': menu, 'menu_items': menu_items})


def prepregnancy(request):
    return render(request, 'parentroadmapapp/prepregnancy.html', {'title': 'Хочу стать родителем', 'menu': menu})


def pregnancy(request):
    return render(request, 'parentroadmapapp/pregnancy.html', {'title': 'Ведение беременности', 'menu': menu})


def parenting(request):
    return render(request, 'parentroadmapapp/parenting.html', {'title': 'Я родитель', 'menu': menu})
