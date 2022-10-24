from django.urls import path
from .views import FoodMenu


urlpatterns = [
    path('', FoodMenu.as_view(), name='menu'),
]
