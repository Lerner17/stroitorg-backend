from rest_framework.routers import DefaultRouter
from .views import MainSliderView, PartnersView, EmployeeViewSet

router = DefaultRouter()
router.register(r'slider', MainSliderView)
router.register(r'partners', PartnersView)
router.register(r'employee', EmployeeViewSet)

urlpatterns = []
urlpatterns += router.urls
