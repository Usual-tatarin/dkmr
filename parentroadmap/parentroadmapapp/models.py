from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    objects = models.Manager()

class Prepregnancy(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    objects = models.Manager()