from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class CompanyView(TemplateView):
    template_name = 'company.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class QuoteView(TemplateView):
    template_name = 'quote.html'