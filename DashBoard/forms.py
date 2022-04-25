from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobOffer
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