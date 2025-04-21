from django.db import models


class Prepregnancy(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    objects = models.Manager()