from django.urls import path
from .views import *

app_name = 'Admin'

urlpatterns = [
    path('', AdminView.as_view(), name='home'),
]