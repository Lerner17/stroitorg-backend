from rest_framework import permissions, viewsets, mixins
from .serializers import MainSliderSerializer, PartnerSerializer, EmployeeSerializer, GallerySerializer, \
    ProjectSerializer, NumberWithTextSerializer, ContactsSerializer, AdvantageSerializer
from .models import MainSlider, Partner, EmployeeCard, Gallery, Project, NumberWithText, Contacts, Advantage
from rest_framework.response import Response


class ContactsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return self.queryset.first()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ContactsSerializer(queryset, many=False)
        return Response(serializer.data)


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


class GalleryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
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
