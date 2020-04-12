from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from news.models import News
from catalog.models import Category
from .serializers import AdminNewsSerializer, UserSerializer, AdminCategorySerializer
from rest_framework import mixins


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email and password:
        try:
            validate_email(email)
            user = authenticate(
                request=request, username=email, password=password)
            if not user:
                return Response({'success': False, 'message': 'Неверный логин или пароль'}, status=400)
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({
                'success': True,
                'token': token.key,
                'user': serializer.data
            }, status=200)
        except ValidationError:
            return Response({'success': False, 'message': 'Не валидный Email'}, status=400)
    else:
        return Response({'success': False, 'message': 'Поля логин и пароль обязательные.'}, status=400)


class AdminCategoryViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = AdminCategorySerializer
    queryset = Category.objects.all()


class AdminNewsViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin):

    permission_classes = (permissions.IsAdminUser, )
    serializer_class = AdminNewsSerializer
    queryset = News.objects.all()
