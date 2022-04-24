from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class AdminView(TemplateView):
    template_name = 'Admin/index.html'