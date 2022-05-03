from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from ..models import Student, Alumni
from ..forms import StudentForm, AlumniForm


class DashBoardView(TemplateView):
    template_name = 'Admin/index.html'


class ProfileView(View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user.id)
            form = StudentForm(instance=student)
            template = 'DashBoard/student/edit.html'
        except:
            alumni = Alumni.objects.get(user=request.user.id)
            form = AlumniForm(instance=alumni)
            template = 'DashBoard/alumni/edit.html'
        return render(request, template, {'form':form})

        