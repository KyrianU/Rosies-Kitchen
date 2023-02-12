from django.contrib import admin
from .models import Customer, Table, Reservation

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email',)


class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_no_people',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'customer', 'no_of_guest', 'table',
                    'date_requested', 'time_requested',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
