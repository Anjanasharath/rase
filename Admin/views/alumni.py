from django.shortcuts import render,redirect
from django.views.generic import ListView
from DashBoard.models import Alumni


class AlumniListView(ListView):
    model = Alumni
    template_name = 'Admin/alumni/list.html'
    context_object_name = 'alumnis'
    paginate_by = 10

    def get_queryset(self):
        return Alumni.objects.all()