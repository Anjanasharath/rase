from django.contrib import messages 
from django.shortcuts import render, redirect
from django.views import View
from ..forms import AlumniForm
from ..models import Alumni


class UpdateAlumniProfile(View):
    def get(self, request):
        try:
            alumni = Alumni.objects.get(user=request.user.id)
            form = AlumniForm(instance=alumni)
            return render(request, 'DashBoard/alumni/edit.html', {'form': form})
        except Alumni.DoesNotExist:
            form = AlumniForm()
            return render(request, 'DashBoard/alumni/add.html', {'form': form})

    def post(self, request):
        data = request.POST.copy()
        data['user'] = request.user.id
        try:
            alumni = Alumni.objects.get(user=request.user.id)
            form = AlumniForm(data, instance=alumni)
        except Alumni.DoesNotExist:
            form = AlumniForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumni Profile Updated Successfully')
            return redirect('DashBoard:alumniProfile')
        return render(request, 'DashBoard/alumni/add.html', {'form': form, 'errors': form.errors})
