from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ThicknessViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'thickness', ThicknessViewSet)

urlpatterns = []
urlpatterns += router.urls
