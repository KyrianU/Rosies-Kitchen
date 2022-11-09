from django import forms
from .models import Reservation, Customer
from django.conf import settings


class CustomerForms(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('full_name', 'email')


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('no_of_guest', 'date_requested', 'time_requested')
