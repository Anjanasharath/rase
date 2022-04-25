from django.contrib import messages 
from django.shortcuts import render, redirect
from django.views import View
from ..forms import StudentForm
from ..models import Student


class UpdateStudentProfile(View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user.id)
            form = StudentForm(instance=student)
            return render(request, 'DashBoard/student/edit.html', {'form': form})
        except Student.DoesNotExist:
            form = StudentForm()
            return render(request, 'DashBoard/student/add.html', {'form': form})

    def post(self, request):
        data = request.POST.copy()
        data['user'] = request.user.id
        try:
            student = Student.objects.get(user=request.user.id)
            form = StudentForm(data, instance=student)
        except Student.DoesNotExist:
            form = StudentForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Profile Updated Successfully')
            return redirect('DashBoard:studentProfile')
        return render(request, 'DashBoard/student/add.html', {'form': form, 'errors': form.errors})