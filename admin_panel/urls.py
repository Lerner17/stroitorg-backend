from rest_framework.routers import DefaultRouter
from .views import AdminNewsViewSet

router = DefaultRouter()
router.register(r'news', AdminNewsViewSet)

urlpatterns = []
urlpatterns += router.urls
