from rest_framework import permissions, viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategoryListSerializer, CategoryDetailSerializer


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
