from django.contrib import admin
from .models import MainSlider, Partner


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass
