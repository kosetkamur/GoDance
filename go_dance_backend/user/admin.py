from django.contrib import admin

from go_dance_backend.user.models import User

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    pass
