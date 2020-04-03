from rest_framework import viewsets, permissions
from news.models import News
from .serializers import AdminNewsSerializer
from rest_framework import mixins


class AdminNewsViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin):

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = AdminNewsSerializer
    queryset = News.objects.all()
