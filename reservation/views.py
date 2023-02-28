from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ReservationForm
from .models import Reservation
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from django.views.generic.edit import FormView


class ReservationFormView(FormView):
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = '/reservation/my_reservation/'

    def form_valid(self, form):
        form = form.save(commit=False)
        user = User.objects.get(username=self.request.user.username)
        form.user = user

        form.save()
        return super().form_valid(form)


class RequestReservationview(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    reservation_success = '/my_reservation'
    reservation_message = 'Booking created'


class ManageReservation(ListView):
    model = Reservation
    template_name = 'my_reservation.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(user=self.request.user)


# Ammend selected or all reservations
class ReservationEdit(SuccessMessageMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'edit_reservation.html'
    success_url = reverse_lazy('my_reservation')
    reservation_message = 'Reservation Updated!'


# Delete selected or all reservations
class ReservationDelete(SuccessMessageMixin, DeleteView):
    model = Reservation
    template_name = 'delete_reservation.html'
    success_url = reverse_lazy('my_reservation')
