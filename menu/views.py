from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Menu


class FoodMenu(ListView):
    """
    Food menus as a lit of items from the database
    """
    model = Menu
    template_name = 'food_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
