from django.urls import path
from .views import *

app_name = 'Admin'

urlpatterns = [
    path('', AdminView.as_view(), name='home'),
    path('events/', EventView.as_view(), name='events'),
    path('events/add', AddEventView.as_view(), name='addEvent'),
    path('events/<int:pk>/edit', EditEventView.as_view(), name='editEvent'),
    path('events/<int:pk>/delete', DeleteEventView.as_view(), name='deleteEvent'),

    path('alumnis/', AlumniListView.as_view(), name='alumnis'),
    path('students/', StudentListView.as_view(), name='students'),

    path('activate/<int:pk>/', ActivateAndDeactivateUserView.as_view(), name='activate_user'),

]