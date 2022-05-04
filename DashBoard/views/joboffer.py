from django.contrib import messages 
from django.shortcuts import render, redirect
from django.views import View
from ..forms import JobOfferForm
from ..models import JobOffer


class AddJobOfferView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = JobOfferForm()
            return render(request, 'DashBoard/job/add.html', {'form': form})
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            data = request.POST.copy()
            data['postedby'] = request.user.id
            form = JobOfferForm(data)
            if form.is_valid():
                form.save()
                return redirect('DashBoard:jobOffer')
            messages.error(request, form.errors)
            return render(request, 'DashBoard/job/add.html', {'form': form, 'errors': form.errors})
        return redirect('/login/')


class AllJobOfferView(View):
    def get(self, request):
        jobs = JobOffer.objects.all()
        return render(request, 'Home/jobs.html', {'jobs': jobs})

class JobOfferView(View):
    def get(self, request):
        if request.user.is_staff:
            jobs = JobOffer.objects.all()
        else:
            jobs = JobOffer.objects.filter(postedby=request.user.id)
        return render(request, 'DashBoard/job/list.html', {'jobs': jobs})


class EditJobOfferView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            job = JobOffer.objects.get(pk=pk)
            form = JobOfferForm(instance=job)
            return render(request, 'DashBoard/job/edit.html', {'form': form, 'job': job})
        return redirect('/login/')

    def post(self, request, pk):
        if request.user.is_authenticated:
            job = JobOffer.objects.get(pk=pk)
            form = JobOfferForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                return redirect('DashBoard:jobOffer')
            return render(request, 'DashBoard/job/edit.html', {'form': form, 'job': job})
        return redirect('/login/')
    

class DeleteJobView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            job = JobOffer.objects.get(pk=pk)
            job.delete()
            return redirect('DashBoard:jobOffer')
        return redirect('/login/')
        
