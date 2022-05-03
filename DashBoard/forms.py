from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'