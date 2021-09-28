from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('service/',ServiceView.as_view(),name='service'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('company/',CompanyView.as_view(),name='company'),
    path('work/',WorkView.as_view(),name='work')
]
