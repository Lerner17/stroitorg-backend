from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from catalog.models import Category, Product
from .serializers import AdminNewsSerializer, UserSerializer, AdminCategorySerializer, AdminProductSerializer, \
    AdminProductCreateSerializer, ChangePasswordSerializer
from rest_framework import mixins


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
    permission_classes = (permissions.IsAdminUser, )

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


class AdminCategoryViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AdminCategorySerializer
    queryset = Category.objects.all()


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
        pass

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
