from django.db import models

# Create your models here.


class Menu(models.Model):
    """
    Menu items Model
    """

    MENU_ITEM = (
        ('Starter', 'starter'),
        ('Main', 'main'),
        ('Drinks', 'drinks'),
        ('Dessert', 'dessert'),
    )

    item = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
