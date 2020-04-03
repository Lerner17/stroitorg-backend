from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/admin/', include('admin_panel.urls')),
    path('api/v1/main/', include('main_page.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
