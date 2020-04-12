from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login, AdminCategoryViewSet, AdminProductViewSet

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)
router.register(r'categories', AdminCategoryViewSet)
router.register(r'products', AdminProductViewSet)

urlpatterns = [
    path('login', login),
]
urlpatterns += router.urls
