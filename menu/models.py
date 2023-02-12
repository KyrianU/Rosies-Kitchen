from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    """
    Menu items Model
    """

    MENU_ITEM = (
        ('Starter', 'starter'),
        ('Main', 'main'),
        ('Dessert', 'dessert'),
    )

    item = models.CharField(max_length=20, choices=MENU_ITEM)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
