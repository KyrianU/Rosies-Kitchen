from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ReservationForm
from .models import Reservation
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class RequestReservationview(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    # reservation_success = '/my_reservations'
    reservation_message = 'Booking created'


class ManageReservation(ListView):

    model = Reservation
    template_name = 'my_reservation.html'


# Ammend selected or all reservations
class ReservationEdit(SuccessMessageMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'edit_reservation.html'
    reservation_sucess = 'my_reservations'
    reservation_message = 'Reservation Updated!'


# Delete selected or all reservations
class ReservationDelete(SuccessMessageMixin, DeleteView):
    model = Reservation
    reservation_success = reverse_lazy('my_reservations')
