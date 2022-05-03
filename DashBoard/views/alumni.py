from django.contrib import messages 
from django.shortcuts import render, redirect
from django.views import View
from ..forms import AlumniForm
from ..models import Alumni


class UpdateAlumniProfile(View):
    def get(self, request):
        alumni = Alumni.objects.get(user=request.user.id)
        form = AlumniForm(instance=alumni)
        return render(request, 'DashBoard/alumni/edit.html', {'form': form})

    def post(self, request):
        data = request.POST.copy()
        data['user'] = request.user.id
        alumni = Alumni.objects.get(user=request.user.id)
        form = AlumniForm(data, instance=alumni)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumni Profile Updated Successfully')
            return redirect('DashBoard:alumniProfile')
        else:
            messages.error(request, 'Alumni Profile Update Failed')
            return redirect('DashBoard:alumniProfile')
