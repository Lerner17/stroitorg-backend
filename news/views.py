from rest_framework import permissions, viewsets, mixins
from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny, )
