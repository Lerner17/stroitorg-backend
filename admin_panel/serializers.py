from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News
from catalog.models import Category, Product, ProductImage, Parameter, ParameterValue


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'username', 'email', 'first_name', 'last_name', 'is_staff')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    @staticmethod
    def validate_new_password(value):
        validate_password(value)
        return value


class AdminNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'content', 'created_at', 'updated_at', 'is_active', 'slug', 'image')


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdminProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class AdminProductSerializer(serializers.ModelSerializer):
    images = AdminProductImageSerializer(many=True)
    parameters = serializers.SerializerMethodField('get_parameters')
    category = serializers.SerializerMethodField('get_category')
    preview = serializers.SerializerMethodField('get_preview_picture')

    @staticmethod
    def get_parameters(product):
        parameter_list = []
        for parameter in Parameter.objects.filter(category=product.category):
            for value in ParameterValue.objects.filter(parameter=parameter):
                if value.product == product:
                    parameter_object = {
                        'id': parameter.id,
                        'name': parameter.name,
                        'value': value.value
                    }
                    parameter_list.append(parameter_object)
        return parameter_list

    @staticmethod
    def get_category(product):
        if product.category:
            category = Category.objects.get(id=product.category.id)
            return {
                'id': category.id,
                'slug': category.slug,
                'name': category.name
            }
        else:
            return []

    @staticmethod
    def get_preview_picture(product):
        preview = None
        for image in ProductImage.objects.filter(product=product.id):
            if image.is_preview:
                preview = image.image.url
        return preview

    class Meta:
        model = Product
        fields = '__all__'


class AdminProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('save_category')

    @staticmethod
    def save_category(category):
        return category.save()

    class Meta:
        model = Product
        fields = '__all__'


class AdminProductImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
