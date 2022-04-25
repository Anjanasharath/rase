from django.urls import path
from .views import *
app_name = 'DashBoard'

urlpatterns = [
    path('', HomeIndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about_us'),
    path('contact/', ContactView.as_view(), name='contact_us'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),

    path('search/', Search.as_view(), name='search'),

    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('events/', EventsView.as_view(), name='events'),

    path('jobs/', AllJobOfferView.as_view(), name='allJobs'),
    path('job/add/', AddJobOfferView.as_view(), name='addJobOffer'),
    path('job/<int:pk>/edit', EditJobOfferView.as_view(), name='editJobOffer'),
]