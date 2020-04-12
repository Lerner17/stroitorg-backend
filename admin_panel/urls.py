from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login, AdminCategoryViewSet, AdminProductViewSet, user_info, UpdatePassword

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)
router.register(r'categories', AdminCategoryViewSet)
router.register(r'products', AdminProductViewSet)

urlpatterns = [
    path('auth/login', login),
    path('auth/user', user_info),
    path('user/update_password', UpdatePassword.as_view()),
]
urlpatterns += router.urls
