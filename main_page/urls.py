from rest_framework.routers import DefaultRouter
from .views import MainSliderView, PartnersView

router = DefaultRouter()
router.register(r'slider', MainSliderView)
router.register(r'partners', PartnersView)

urlpatterns = []
urlpatterns += router.urls
