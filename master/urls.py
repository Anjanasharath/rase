from django.urls import path, include
from master.views import HomeView
urlpatterns = [
        path('', HomeView.as_view(), name='home'),
    ]