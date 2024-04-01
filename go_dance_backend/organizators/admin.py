from django.contrib import admin

from go_dance_backend.organizators.models import Organizator, Company, Teacher, TeacherStyle

@admin.register(Organizator)
class OrganizatorAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(TeacherStyle)
class TeacherStyleAdmin(admin.ModelAdmin):
    pass