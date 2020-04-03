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


# partners model
class Partner(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    logo = ProcessedImageField(
        upload_to='partners/',
        processors=[ResizeToFit(200, 90)],
        verbose_name='Логотип'
    )
    url = models.URLField(max_length=255, verbose_name='Сайт партнёра')
