from django.contrib import admin
from .models import Product, ProductImage, Category


admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Product)
