from django.urls import path
from .import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.ReservationFormView.as_view(), name='reservation'),
    path('my_reservation/', views.ManageReservation.as_view(),
         name='my_reservation'),
    path('edit_reservation/', views.ReservationEdit.as_view(),
         name='edit_reservation'),
    path('delete_reservation/', views.ReservationDelete.as_view(),
         name='delete_reservation')

]
