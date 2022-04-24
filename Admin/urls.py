from django.urls import path
from .views import *


urlpatterns = [
    path('', AdminView.as_view(), name='home'),
]