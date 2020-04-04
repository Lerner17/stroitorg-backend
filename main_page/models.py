from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# main slider model
class MainSlider(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    text = models.CharField(max_length=255, verbose_name='Описание')
    image = ProcessedImageField(
        upload_to='main_slider/',
        processors=[ResizeToFit(1280, 720)],
        verbose_name='Изображение'
    )
    url = models.URLField(max_length=255, verbose_name='Подробнее по ссылке')

    def __str__(self):
        return self.title


# partners model
class Partner(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    logo = ProcessedImageField(
        upload_to='partners/',
        processors=[ResizeToFit(200, 90)],
        verbose_name='Логотип'
    )
    url = models.URLField(max_length=255, verbose_name='Сайт партнёра')

    def __str__(self):
        return self.name


class EmployeeCard(models.Model):

    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    position = models.CharField(max_length=32, blank=False)
    bio = models.TextField(blank=True)
    avatar = ProcessedImageField(
        upload_to='avatars/',
        processors=[ResizeToFit(167, 162)],
        verbose_name='Фото сотрудника'
    )
    email = models.EmailField(max_length=255, blank=True, null=True)
