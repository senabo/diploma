from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('scan/', TagScan.as_view()),
    path('register/', TagRegistration.as_view()),
]
