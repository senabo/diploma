from django.contrib import admin
from django.urls import path, include
from app.admin import tracker_admin
from app.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', tracker_admin.urls),
    path('', index, name = 'index' ),
    path('api/', include('app.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)