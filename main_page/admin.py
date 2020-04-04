from django.contrib import admin
from .models import MainSlider, Partner, EmployeeCard

admin.site.register(EmployeeCard)


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass
