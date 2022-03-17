from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'master/home.html'


class AboutUsView(TemplateView):
    template_name = 'master/aboutus.html'
