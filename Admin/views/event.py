from dataclasses import field
from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from ..models import Event
from ..forms import EventForm

# Create your views here.
class EventView(View):
    def get(self, request):
        events = Event.objects.all()
        context = {
            'header': 'Events',
            'events': events,
        }
        return render(request, 'Admin/events/events.html', context)

class AddEventView(View):
    def get(self, request):
        form = EventForm()
        context = {
            'header': 'Add Event',
            'form': form
        }
        return render(request, 'Admin/events/create.html', context)
    
    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Admin:Events')
        return render(request, 'Admin/events/create.html', {'form': form})

class EditEventView(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        form = EventForm(instance=event)
        context = {
            'header': 'Edit Event',
            'form': form
        }
        return render(request, 'Admin/events/edit.html', context)

    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
        return render(request, 'Admin/edit.html', {'form': form})

    def delete(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return render(request, 'Admin/events/events.html')

