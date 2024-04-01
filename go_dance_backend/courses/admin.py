from django.contrib import admin

from go_dance_backend.courses.models import Course

@admin.register(Course)
class CourseAdmin (admin.ModelAdmin):
    pass