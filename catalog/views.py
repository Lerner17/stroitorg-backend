from django.core.mail import send_mail
from rest_framework import permissions, viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Category, Order, Thickness
from .serializers import ProductSerializer, CategoryListSerializer, CategoryDetailSerializer, OrderSerializer, ThicknessSerializer


class ThicknessViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Thickness.objects.all()
    serializer_class = ThicknessSerializer
    permission_classes = (permissions.AllowAny, )


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    search_fields = ['name', 'description', 'category__name']
    filter_backends = (filters.SearchFilter, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = PageNumberPagination
    DEFAULT_PAGINATION_COUNT = 10
    ordering_fields = ['id']

    def get_serializer_class(self):
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        self.pagination_class.page_size = self.get_paginated_count()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_paginated_count(self):
        count = self.request.GET.get('count')
        if count is None:
            return self.DEFAULT_PAGINATION_COUNT
        else:
            return count


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        else:
            return CategoryDetailSerializer

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        product_id_list = [product['id']
                           for product in request.data['products']]
        product_list = request.data['products']
        buyer_name = request.data.get('buyer_name', 'No name')
        buyer_phone = request.data.get('buyer_phone', 'No phone')
        comment = request.data.get('comment', 'No comment')
        serializer_data = {
            "buyer_name": buyer_name,
            "buyer_phone": buyer_phone,
            "comment": comment,
            "products": product_id_list
        }

        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        products = Product.objects.filter(pk__in=product_id_list)
        product_message = ''
        total_price = 0
        for product in products:
            for count in product_list:
                if product.id == count['id']:
                    price = product.price * count['count']
                    total_price += price
                    product_message += f'{product.name} - {count["count"]} - {str(price)}\n'

        subject = 'Новый заказ'
        message = f'Имя покупателя: {buyer_name}\n Номер покупателя: {buyer_phone}\n Комментарий: {comment}\n Список ' \
                  f'товаров: {product_message}\n Общая стоимость: {total_price}'
        mail_from = 'site@example.com'
        mail_to = ('admin@example.com', )
        # send_mail(subject, message, mail_from, mail_to)
        return Response(message)

