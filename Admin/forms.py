from django.forms.models import ModelForm
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location']