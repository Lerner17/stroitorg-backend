from rest_framework import permissions, viewsets, mixins
from .serializers import MainSliderSerializer, PartnerSerializer
from .models import MainSlider, Partner


class MainSliderView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = MainSlider.objects.all()
    serializer_class = MainSliderSerializer
    permission_classes = (permissions.AllowAny, )


class PartnersView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (permissions.AllowAny, )
