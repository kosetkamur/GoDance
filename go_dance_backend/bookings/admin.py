from django.contrib import admin

from go_dance_backend.bookings.models import Booking

@admin.register(Booking)
class BookingAdmin (admin.ModelAdmin):
    pass