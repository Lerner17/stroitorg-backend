from rest_framework import permissions, viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )
