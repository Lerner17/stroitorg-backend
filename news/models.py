from django.db import models
from slugify import slugify

class News(models.Model):

    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news_images', blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        elif not self.id:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)