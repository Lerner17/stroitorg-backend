from rest_framework import serializers
from .models import MainSlider, Partner


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ('title', 'text', 'image', 'url')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('name', 'logo', 'url')
