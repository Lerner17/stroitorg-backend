from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login, AdminCategoryViewSet, AdminProductViewSet, user_info

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)
router.register(r'categories', AdminCategoryViewSet)
router.register(r'products', AdminProductViewSet)

urlpatterns = [
    path('auth/login', login),
    path('auth/user', user_info),
]
urlpatterns += router.urls
