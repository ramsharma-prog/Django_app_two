from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import time


class HomePage(generic.TemplateView):
    template_name = 'home.html'


class WelcomePage(generic.TemplateView):
    template_name = 'welcome.html'


class ByePage(generic.TemplateView):
    template_name = 'home.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'
