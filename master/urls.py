from django.urls import path, include
from master.views import AboutUsView, HomeView
urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('aboutus', AboutUsView.as_view(), name='aboutus'),
    ]