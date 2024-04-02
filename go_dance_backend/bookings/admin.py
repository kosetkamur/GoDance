from django.contrib import admin

from go_dance_backend.bookings.models import Booking, Seance


@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
