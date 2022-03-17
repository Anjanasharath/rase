from django.urls import path, include
from userprofile.views import UserRegisterView, UserLogoutView

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register')
]
