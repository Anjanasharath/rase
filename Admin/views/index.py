from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


class AdminView(TemplateView):
    template_name = 'Admin/index.html'


class ActivateAndDeactivateUserView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.is_active:
            user.is_active = False
            user.save()
            messages.success(request, f"User {user.username} has been deactivated.")
        else:
            user.is_active = True
            user.save()
            messages.success(request, f"User {user.username} has been activated.")
        return redirect()

