from django.db import models
from django.db.models import IntegerField, AutoField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


time_choices = (
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
    ("22:00", "22:00"),
)


class Reservation(models.Model):
    table_seats = models.IntegerField(
        blank=False,
        null=False,
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4),
        ]
    )
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, null=True)
    date = models.DateField()
    time = models.CharField(
        max_length=20, choices=time_choices, default="12:00")
    date_booked = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.reservation_id)
