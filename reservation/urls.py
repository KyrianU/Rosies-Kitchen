from django.urls import path
from reservation import views


urlpatterns = [
    path('', views.RequestReservationview.as_view(), name='reservation'),
    path('manage_myreservations', views.ManageReservation.as_view(),
         name='manage_reservations'),
    path('edit_reservation', views.ReservationEdit.as_view(),
         name='edit_reservation'),
    path('delete_reservation', views.ReservationDelete.as_view(),
         name='delete_reservation')

]
