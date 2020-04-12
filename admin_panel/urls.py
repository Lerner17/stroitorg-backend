from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login, AdminCategoryViewSet

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)
router.register(r'categories', AdminCategoryViewSet)

urlpatterns = [
    path('login', login),
]
urlpatterns += router.urls
