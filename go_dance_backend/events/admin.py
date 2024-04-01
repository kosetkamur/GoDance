from django.contrib import admin

from go_dance_backend.events.models import Event

@admin.register(Event)
class EventAdmin (admin.ModelAdmin):
    pass