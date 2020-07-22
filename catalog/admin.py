from django.contrib import admin
from .models import Product, ProductImage, Category, Parameter, Thickness

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Parameter)
admin.site.register(Thickness)
