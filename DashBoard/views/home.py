from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from Admin.models import Event

# Create your views here.
class HomeIndexView(View):
    def get(self, request):
        return render(request, 'Home/home.html')


class AboutView(TemplateView):
    template_name = 'Home/aboutus.html'


class ContactView(TemplateView):
    template_name = 'Home/contactus.html'


class Search(TemplateView):
    template_name = 'Home/search.html'


class EventsView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'Home/events.html', {'events': events})