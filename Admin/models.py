from django.db import models


# Create your models here.
class Event(models.Model):
    TYPE = (
        ('Alumni meet', 'Alumni meet'),
        ('Training', 'Training'),
        ('Event', 'Event'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
