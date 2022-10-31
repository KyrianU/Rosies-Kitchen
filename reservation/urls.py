from django.urls import path


class RequestReservationview(BookingSuccesful, Create_booking):
    model = reservation
    form = Reservationform
    template_name = 'create_reservation_form.html'
    reservation_success = '/my_reservations'
    reservation_message = 'Booking created'


