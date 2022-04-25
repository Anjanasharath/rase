from django.db import models

# Create your models here.
class JobOffer(models.Model):
    title = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    eligibilities = models.TextField()
    salary = models.CharField(max_length=100)
    lastdate = models.DateField()
    reference = models.CharField(max_length=100, null=True)
    applyurl = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title