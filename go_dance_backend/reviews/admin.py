from django.contrib import admin

from go_dance_backend.reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass