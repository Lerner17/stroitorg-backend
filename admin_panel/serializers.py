from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from news.models import News
from catalog.models import Category, Product, ProductImage, Parameter, Thickness
from main_page.models import MainSlider, Partner, EmployeeCard, Advantage, Project, NumberWithText, Gallery, Contacts
from orders.models import Order, OrderProduct

from catalog.serializers import ProductSerializer


class OrderProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity', 'product')


class OrderDetailSerializer(serializers.ModelSerializer):

    items = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'phone', 'items', 'is_delivered')


class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()
    items_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'first_name', 'phone', 'total_price',
                  'items_count', 'is_delivered')

    def get_total_price(self, obj):
        total_price = 0
        for item in obj.items.all():
            total_price += item.product.price * item.quantity
        return total_price

    def get_items_count(self, obj):
        return obj.items.count()


class ThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thickness
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'username',
                  'email', 'first_name', 'last_name', 'is_staff')


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
        fields = ('id', 'title', 'description', 'content',
                  'created_at', 'updated_at', 'is_active', 'slug', 'image')


class AdminMainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = '__all__'


class AdminPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class AdminEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCard
        fields = '__all__'


class AdminAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class AdminGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class AdminProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AdminNumberWithTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberWithText
        fields = '__all__'


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdminProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class ContactsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class AdminParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ('name', 'value')


class AdminParameterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'


class AdminProductSerializer(serializers.ModelSerializer):
    images = AdminProductImageSerializer(many=True)
    parameters = AdminParameterSerializer(many=True)
    category = serializers.SerializerMethodField('get_category')
    preview = serializers.SerializerMethodField('get_preview_picture')

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
    parameters = AdminParameterSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class AdminProductImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class AdminProductCreateSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('save_category')
    # image = AdminProductImageCreateSerializer(many=True)

    @staticmethod
    def save_category(category):
        return category.save()

    class Meta:
        model = Product
        fields = '__all__'
