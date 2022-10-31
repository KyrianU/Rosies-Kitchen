from django.db import models
from djanog.db.models import Intergerfield

# Create your models here.


class Customer(models.model):
    """
    Customer details model
    """
    customer_id = models.Autofield(primary_key=True)
    full_name = models.Charfield(max_length=60)
    email = models.EmailField(max_length=200, defaults="")
    phone_number = models.PhoneNumberField(null=True)

    def __str__(self):
        return str(self.full_name)


class Table(models.Model):
    """
    Table Model
    """
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()
    table_name = models.CharField(
        max_length=15, default='New Table', unique=True)

    def __str__(self):
        return str(self.table_name)


class Reservation(models.Model):
    """
    Reservation model,
    """
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True)
    date_requested = models.DateField()
    time_requested = models.TimeField()

    def __str__(self):
        return str(self.reservation_id)
