from django.shortcuts import render
from .models import Prepregnancy, Pregnancy, Parenting, Menu

menu_items_prepregnancy = Prepregnancy.objects.values('title', 'slug')
menu_items_pregnancy = Pregnancy.objects.values('title', 'slug')
menu_items_parenting = Parenting.objects.values('title', 'slug')
menu = Menu.objects.values('title', 'url')


def index(request):
    return render(request, 'parentroadmapapp/index.html',
                  {'title': 'Главная страница', 'menu': menu})


def prepregnancy(request):
    return render(request, 'parentroadmapapp/prepregnancy.html',
                  {'title': 'Хочу стать родителем', 'menu': menu, 'menu_items': menu_items_prepregnancy})


def pregnancy(request):
    return render(request, 'parentroadmapapp/pregnancy.html',
                  {'title': 'Ведение беременности', 'menu': menu, 'menu_items': menu_items_pregnancy})


def parenting(request):
    return render(request, 'parentroadmapapp/parenting.html',
                  {'title': 'Я родитель', 'menu': menu, 'menu_items': menu_items_parenting})


def post(request, slug):
    return render(request, 'parentroadmapapp/post.html',
                  {'title': 'Статья', 'menu': menu})
