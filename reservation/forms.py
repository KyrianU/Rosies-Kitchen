from django import forms
from .models import Reservation, Customer
from django.conf import settings
from django.core.exceptions import ValidationError


class CustomerForms(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('full_name', 'email')


class ReservationForm(forms.ModelForm):

    # compare user input against current date and raise an error message
    # if date is in the past
    def clean_start_time(self):
        start = self.cleaned_data('date')
        if start < datetime.date.now():
            raise forms.ValidationError('the date cannot be in the past.')
        return data

    class Meta:
        model = Reservation
        fields = ('name', 'no_of_guest', 'date_requested', 'time_requested')
        widget = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }


class ReservationsEdit(forms.ModelForm):

    # compare user input against current date and raise an error message
    # if date is in the past
    def clean_start_time(self):
        start = self.cleaned_data('date')
        if start < datetime.date.now():
            raise forms.ValidationError('the date cannot be in the past.')
        return data

    class Meta:
        model = Reservation
        fields = ('name', 'no_of_guest', 'date_requested', 'time_requested')
        widget = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }
