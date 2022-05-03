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
    postedby = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    course = models.CharField(max_length=100)
    dob = models.DateField()
    courseDuration = models.IntegerField()
    tenthPercentage = models.IntegerField()
    twelthPercentage = models.IntegerField()
    contactNo = models.CharField(max_length=13)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)


class Alumni(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    courseDeatils = models.CharField(max_length=100)
    yearOfPassing = models.IntegerField()
    yearOfJoining = models.IntegerField()
    jobStatus = models.CharField(max_length=100)
    contactNo = models.CharField(max_length=13)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Reply(models.Model):
    reply = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.Case)
