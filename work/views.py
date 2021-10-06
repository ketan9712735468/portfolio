from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.contrib import messages

from work.models import Contact

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class ContactView(RedirectView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request,'contact.html')

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name,email=email,subject=subject,message=message)
        except:
            messages.error(request,'email is already taken')            
        return self.get(request, *args, **kwargs)


class CompanyView(TemplateView):
    template_name = 'company.html'

class WorkView(TemplateView):
    template_name = 'work.html'