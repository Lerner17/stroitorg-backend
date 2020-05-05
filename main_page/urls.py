from rest_framework.routers import DefaultRouter
from .views import MainSliderViewSet, PartnersViewSet, EmployeeViewSet, AdvantageViewSet, ProjectViewSet, \
    NumberWithTextViewSet, ContactsViewSet

router = DefaultRouter()
router.register(r'slider', MainSliderViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'advantage', AdvantageViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'numbers', NumberWithTextViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = []
urlpatterns += router.urls
