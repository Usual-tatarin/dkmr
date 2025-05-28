from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('prepregnancy/', views.prepregnancy, name='prepregnancy'),
    path('pregnancy/', views.pregnancy, name='pregnancy'),
    path('parenting/', views.parenting, name='parenting'),
    path('post/<slug:slug>/', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

