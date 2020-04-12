from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News
from catalog.models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff')


class AdminNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'content', 'created_at', 'updated_at', 'is_active', 'slug', 'image')


class AdminCategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
