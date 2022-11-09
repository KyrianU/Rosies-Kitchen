from django.db import models
from django.db.models import IntegerField


# Create your models here.


class Customer(models.Model):
    """
    Customer detail model
    """
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=200, default="")

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

    def validate_date(reservation_time_and_date):
        """
        function to validate date
        so that booking cannot be
        in the past
        """
        if reservation_time_and_date < date.now():
            raise ValidationError(
                message='Date cannot be in the past'
            )

    """
    Reservation model,
    """
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True)
    guest_choices = [(1, "1 person"), (2, "2 people"),
                     (3, "3 people"), (4, "4 people"),
                     (5, "5 people"), (6, "6 people")]
    no_of_guest = models.IntegerField(choices=guest_choices, default=1)
    date_requested = models.DateField()
    time_requested = models.TimeField()

    def __str__(self):
        return str(self.reservation_id)
