from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from slugify import slugify


class Category(models.Model):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.name)
        elif not self.id:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Thickness(models.Model):
    thickness = models.PositiveIntegerField(blank=False)


class Product(models.Model):
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(
        Category, null=True, related_name='products', on_delete=models.SET_NULL)
    name = models.CharField(max_length=127)
    description = models.TextField()
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField(null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    thickness = models.ForeignKey(
        Thickness, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        elif not self.id:
            self.slug = slugify(self.slug)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = ProcessedImageField(
        upload_to='products/',
        processors=[ResizeToFit(500, 500)]
    )
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE)
    is_preview = models.BooleanField(default=False)


class Parameter(models.Model):
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=128)
    product = models.ForeignKey(
        Product, null=True, related_name='parameters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer_name = models.CharField(max_length=64)
    buyer_phone = models.CharField(max_length=16)
    comment = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='order')


# class ParameterValue(models.Model):
#     parameter = models.ForeignKey(Parameter, related_name='values', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,
#                                 related_name='parameters',
#                                 on_delete=models.CASCADE)
#     value = models.CharField(max_length=32)
#
#     def __str__(self):
#         return str(self.parameter.name + ' ' + self.product.name)
