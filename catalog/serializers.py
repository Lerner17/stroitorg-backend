from rest_framework import serializers
from .models import Product, ProductImage, Category, ParameterValue, Parameter


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
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


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_products')
    children = serializers.SerializerMethodField('get_children')
    parents = serializers.SerializerMethodField('get_parents')

    @staticmethod
    def get_products(category):
        product_list = []
        for product in Product.objects.filter(category=category.id):
            product_object = {
                'id': product.id,
                'slug': product.slug,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'new_price': product.new_price,
                'is_new': product.is_new,
                'is_discount': product.is_discount
            }
            product_list.append(product_object)
        return product_list

    @staticmethod
    def get_parents(category):
        is_have_parent = False if not category.parent else True
        parent_list = []
        parent = {}
        if is_have_parent:
            parent = category.parent
        while is_have_parent:
            parent_object = {
                'id': parent.id,
                'slug': parent.slug,
                'name': parent.name
            }
            parent_list.append(parent_object)
            if parent.parent:
                parent = parent.parent
            else:
                is_have_parent = False
        return parent_list

    @staticmethod
    def get_children(category):
        children_list = []
        for child in Category.objects.filter(parent=category):
            child_object = {
                'id': child.id,
                'slug': child.slug,
                'name': child.name
            }
            children_list.append(child_object)
        return children_list

    class Meta:
        model = Category
        fields = '__all__'
