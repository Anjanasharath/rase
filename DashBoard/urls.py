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
    path('events', EventsView.as_view(), name='events'),

    path('jobs/', AllJobOfferView.as_view(), name='allJobs'),
    path('job/', JobOfferView.as_view(), name='jobOffer'),
    path('job/add/', AddJobOfferView.as_view(), name='addJobOffer'),
    path('job/<int:pk>/edit', EditJobOfferView.as_view(), name='editJobOffer'),
    path('job/<int:pk>/delete', DeleteJobView.as_view(), name='deleteJobOffer'),

    path('Gallery/', AllGalleryView.as_view(), name='allGallery'),
    path('gallery/', ListGalleryView.as_view(), name='listGallery'),
    path('gallery/add/', AddGalleryView.as_view(), name='addGallery'),
    path('gallery/<int:pk>/delete', DeleteGalleryView.as_view(), name='deleteGallery'),
    path('gallery/<int:pk>/edit', EditGalleryView.as_view(), name='editGallery'),

    path('question/', ListQuestionView.as_view(), name='question'),
    path('question/<int:pk>', QuestionView.as_view(), name='viewQuestion'),
    path('question/add/', AddQuestionView.as_view(), name='addQuestion'),
    path('question/<int:pk>/edit', EditQuestionView.as_view(), name='editQuestion'),
    path('question/<int:pk>/delete', DeleteQuestionView.as_view(), name='deleteQuestion'),



    path('profile/student', UpdateStudentProfile.as_view(), name='studentProfile'),
    path('profile/alumni', UpdateAlumniProfile.as_view(), name='alumniProfile'),

    path('profile/', ProfileView.as_view(), name='profile')
]