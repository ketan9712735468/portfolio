from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('services/',ServiceView.as_view(),name='home'),
    path('company/',CompanyView.as_view(),name='home'),
    path('contact-us/',ContactView.as_view(),name='home'),
    path('request-a-quote/',QuoteView.as_view(),name='home'),
]
# + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
