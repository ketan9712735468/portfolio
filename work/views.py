from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CompanyView(TemplateView):
    template_name = 'company.html'

class WorkView(TemplateView):
    template_name = 'work.html'