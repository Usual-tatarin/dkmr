from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name='URL')
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if self.title.lower() == 'главная страница' and not self.url:
            self.url = '/'  # Для главной страницы URL равен '/'
        super().save(*args, **kwargs)


class Prepregnancy(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    menu = models.ForeignKey(
        Menu,  # Связь с моделью Category
        on_delete=models.CASCADE,  # При удалении категории удаляются все связанные статьи
        related_name='prepregnancy_menu',  # Имя для обратной связи
        null=True
    )

    objects = models.Manager()


class Pregnancy(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    menu = models.ForeignKey(
        Menu,  # Связь с моделью Category
        on_delete=models.CASCADE,  # При удалении категории удаляются все связанные статьи
        related_name='pregnancy_menu',  # Имя для обратной связи
        null=True
    )

    objects = models.Manager()


class Parenting(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    menu = models.ForeignKey(
        Menu,  # Связь с моделью Category
        on_delete=models.CASCADE,  # При удалении категории удаляются все связанные статьи
        related_name='parenting_menu',  # Имя для обратной связи
        null=True
    )

    objects = models.Manager()
