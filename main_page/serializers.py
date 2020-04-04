from rest_framework import serializers
from .models import MainSlider, Partner, EmployeeCard, Advantage


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCard
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'
