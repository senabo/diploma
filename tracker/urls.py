from django.contrib import admin
from django.urls import path, include
from app.admin import tracker_admin
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon.ico'), name='favicon'),
    path('admin/', tracker_admin.urls),
    path('api/', include('app.urls')),
    path('', index, name = 'index' ),
    path('student/<pk>/', student_detail, name='student_detail' ),

]


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)