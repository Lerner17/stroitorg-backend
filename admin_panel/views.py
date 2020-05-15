from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.serializers import CategoryListSerializer
from main_page.models import MainSlider, Partner, EmployeeCard, Advantage, Project, NumberWithText, Contacts, Gallery
from news.models import News
from catalog.models import Category, Product, ProductImage
from .serializers import AdminNewsSerializer, UserSerializer, AdminCategorySerializer, AdminProductSerializer, \
    AdminProductCreateSerializer, ChangePasswordSerializer, AdminMainSliderSerializer, AdminPartnerSerializer, \
    AdminEmployeeSerializer, AdminAdvantageSerializer, AdminProjectSerializer, AdminNumberWithTextSerializer, \
    AdminProductImageCreateSerializer, \
    AdminParameterSerializer, AdminParameterCreateSerializer, ContactsAdminSerializer, AdminGallerySerializer

from rest_framework import mixins


class AdminContactsAPIView(views.APIView):

    def get(self, request):
        if not Contacts.objects.exists():
            return Response({
                'twitter_url': None,
                'intagram_url': None,
                'vk_url': None,
                'fb_url': None,
                'phone': None,
                'email': None,
                'address': None
            })
        else:
            serializer = ContactsAdminSerializer(
                Contacts.objects.first(), many=False)
            return Response(serializer.data)

    def put(self, request):
        queryset = Contacts.objects.first()
        if not Contacts.objects.exists():
            serializer = ContactsAdminSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        serializer = ContactsAdminSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = authenticate(
            request=request, username=username, password=password)
        if not user:
            return Response({'success': False, 'message': 'Неверный логин или пароль'}, status=400)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({
            'success': True,
            'token': token.key,
            'user': serializer.data
        }, status=200)
    else:
        return Response({'success': False, 'message': 'Поля логин и пароль обязательные.'}, status=400)


@csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_info(request):
    try:
        token_header = request.headers['Authorization']
    except KeyError:
        return Response({'success': False, 'message': 'Вы не авторизованы.'}, status=400)

    try:
        token = token_header.split()[1]
    except IndexError:
        return Response({'success': False, 'message': 'Неверный токен.'}, status=400)

    token_object = Token.objects.get(pk=token)
    serializer = UserSerializer(token_object.user)

    return Response({
        'success': True,
        'token': token,
        'user': serializer.data
    }, status=200)


class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=400)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'success': True, 'message': 'Пароль успешно изменен.'}, status=200)

        return Response(serializer.errors, status=400)


class AdminUserViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AdminCategoryViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AdminCategorySerializer
        else:
            return self.serializer_class


class AdminProductViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminProductSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    DEFAULT_PAGINATION_COUNT = 10
    ordering_fields = ['id']

    def perform_create(self, serializer):
        category = Category.objects.get(
            pk=self.request.data.get('category_id'))
        serializer.save(category=category)

    def create(self, request, *args, **kwargs):
        parameters = request.data.get('parameters', False)
        # parameters = request.data['parameters']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if parameters:
            parameters_to_db = []
            for parameter in parameters:
                parameter_object = {
                    'name': parameter['name'],
                    'value': parameter['value'],
                    'product': serializer.data['id']
                }
                parameters_to_db.append(parameter_object)
            param_ser = AdminParameterCreateSerializer(
                data=parameters_to_db, many=True)
            param_ser.is_valid(raise_exception=True)
            param_ser.save()

        # images_to_db = []

        # for image in request.FILES['images']:
        # image_data = {
        #     'image': request.FILES['image'],
        #     'product': serializer.data['id'],
        #     'is_preview': True
        # }
        #     # images_to_db.append(image_data)
        # img_ser = AdminProductImageCreateSerializer(data=image_data)
        # img_ser.is_valid(raise_exception=True)
        # img_ser.save()

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'create':
            return AdminProductCreateSerializer
        else:
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


class AdminNewsViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminNewsSerializer
    queryset = News.objects.all()


class AdminMainSliderViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminMainSliderSerializer
    queryset = MainSlider.objects.all()


class AdminPartnerViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminPartnerSerializer
    queryset = Partner.objects.all()


class AdminEmployeeViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminEmployeeSerializer
    queryset = EmployeeCard.objects.all()


class AdminAdvantageViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminAdvantageSerializer
    queryset = Advantage.objects.all()


class AdminGalleryViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminGallerySerializer
    queryset = Gallery.objects.all()


class AdminProjectViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminProjectSerializer
    queryset = Project.objects.all()


class AdminNumberWithTextViewSet(viewsets.GenericViewSet,
                                 mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminNumberWithTextSerializer
    queryset = NumberWithText.objects.all()
