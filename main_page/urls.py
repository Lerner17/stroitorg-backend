from rest_framework.routers import DefaultRouter
from .views import MainSliderViewSet, PartnersViewSet, EmployeeViewSet, AdvantageViewSet

router = DefaultRouter()
router.register(r'slider', MainSliderViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'advantage', AdvantageViewSet)

urlpatterns = []
urlpatterns += router.urls
