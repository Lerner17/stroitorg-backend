from rest_framework import permissions, viewsets, mixins
from .serializers import MainSliderSerializer, PartnerSerializer, EmployeeSerializer, AdvantageSerializer, \
    ProjectSerializer, NumberWithTextSerializer
from .models import MainSlider, Partner, EmployeeCard, Advantage, Project, NumberWithText


class MainSliderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = MainSlider.objects.all()
    serializer_class = MainSliderSerializer
    permission_classes = (permissions.AllowAny, )


class PartnersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (permissions.AllowAny, )


class EmployeeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny, )


class AdvantageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer
    permission_classes = (permissions.AllowAny, )


class ProjectViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny, )


class NumberWithTextViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = NumberWithText.objects.all()
    serializer_class = NumberWithTextSerializer
    permission_classes = (permissions.AllowAny, )
