from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class WorkView(TemplateView):
    template_name = 'work.html'