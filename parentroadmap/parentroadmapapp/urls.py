from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prepregnancy/<slug:slug>/', views.prepregnancy, name='prepregnancy'),
    path('pregnancy/', views.pregnancy, name='pregnancy'),
    path('parenting/', views.parenting, name='parenting'),
]