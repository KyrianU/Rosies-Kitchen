from django.views.generic import TemplateView
from django.urls import path


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
