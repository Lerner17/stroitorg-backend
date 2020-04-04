from rest_framework import permissions, viewsets, mixins
from .serializers import MainSliderSerializer, PartnerSerializer, EmployeeSerializer
from .models import MainSlider, Partner, EmployeeCard


class MainSliderView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = MainSlider.objects.all()
    serializer_class = MainSliderSerializer
    permission_classes = (permissions.AllowAny, )


class PartnersView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (permissions.AllowAny, )


class EmployeeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeSerializer
    permissions = (permissions.AllowAny, )
