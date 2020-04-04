from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Product model
from slugify import slugify


class Product(models.Model):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=127)
    description = models.TextField()
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField(null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.name)
        elif not self.id:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)
