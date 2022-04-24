from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


class DashBoardView(TemplateView):
    template_name = 'DashBoard/dashboard.html'
