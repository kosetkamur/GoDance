from django.contrib import admin

from go_dance_backend.styles.models import Style

@admin.register(Style)
class StyleAdmin (admin.ModelAdmin):
    pass
