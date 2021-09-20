from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('blog/',BlogView.as_view(),name='blog'),
    path('work/',WorkView.as_view(),name='work')
]
# + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
