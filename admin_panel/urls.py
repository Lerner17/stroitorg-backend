from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)

urlpatterns = [
    path('login', login),
]
urlpatterns += router.urls
