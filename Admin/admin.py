from django.contrib import admin
from .models import Event

# Register your models here.
mymodels = [Event]
admin.site.register(mymodels)