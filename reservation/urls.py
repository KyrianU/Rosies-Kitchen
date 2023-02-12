from django.urls import path
from reservation import views


urlpatterns = [
    path('', views.RequestReservationview.as_view(), name='reservation'),
    path('my_reservations', views.ManageReservation.as_view(),
         name='my_reservations'),
    path('edit_reservation', views.ReservationEdit.as_view(),
         name='edit_reservation'),
    path('delete_reservation', views.ReservationDelete.as_view(),
         name='delete_reservation')

]
