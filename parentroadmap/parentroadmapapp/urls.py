from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prepregnancy/', views.prepregnancy, name='prepregnancy'),
    path('pregnancy/', views.pregnancy, name='pregnancy'),
    path('parenting/', views.parenting, name='parenting'),
    path('post/<slug:slug>/', views.post, name='post'),
]