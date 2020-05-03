from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AdminNewsViewSet, login, AdminCategoryViewSet, AdminProductViewSet, user_info, UpdatePassword, \
    AdminMainSliderViewSet, AdminPartnerViewSet, AdminEmployeeViewSet, AdminAdvantageViewSet, AdminProjectViewSet, \
    AdminNumberWithTextViewSet, AdminUserViewSet

router = DefaultRouter()
router.register(r'users', AdminUserViewSet)
router.register(r'news', AdminNewsViewSet)
router.register(r'main_slider', AdminMainSliderViewSet)
router.register(r'partners', AdminPartnerViewSet)
router.register(r'employee', AdminEmployeeViewSet)
router.register(r'advantages', AdminAdvantageViewSet)
router.register(r'projects', AdminProjectViewSet)
router.register(r'number_with_text', AdminNumberWithTextViewSet)
router.register(r'categories', AdminCategoryViewSet)
router.register(r'products', AdminProductViewSet)

urlpatterns = [
    path('auth/login', login),
    path('auth/user', user_info),
    path('user/update_password', UpdatePassword.as_view()),
]
urlpatterns += router.urls
