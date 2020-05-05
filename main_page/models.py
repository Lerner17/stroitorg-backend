from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# main slider model
from slugify import slugify


class Contacts(models.Model):
    twitter_url = models.URLField(null=True, blank=True)
    intagram_url = models.URLField(null=True, blank=True)
    vk_url = models.URLField(null=True, blank=True)
    fb_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)


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

    def __str__(self):
        return self.first_name


class Advantage(models.Model):
    title = models.CharField(max_length=64)
    image = ProcessedImageField(
        upload_to='advantages/',
        processors=[ResizeToFit(350, 270)]
    )


class Project(models.Model):
    title = models.CharField(max_length=127)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    image = ProcessedImageField(
        upload_to='projects/',
        processors=[ResizeToFit(400, 470)]
    )

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        elif not self.id:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)


class NumberWithText(models.Model):
    text = models.CharField(max_length=32)
    number = models.PositiveIntegerField()
