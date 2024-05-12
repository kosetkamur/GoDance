from django.contrib import admin

from go_dance_backend.organizators.models import Organizator, Company, Teacher, TeacherStyle

@admin.register(Organizator)
class OrganizatorAdmin(admin.ModelAdmin):
    pass

class TeacherCompanyInline(admin.TabularInline):
    model = Company.teachers.through

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [TeacherCompanyInline]
    pass
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(TeacherStyle)
class TeacherStyleAdmin(admin.ModelAdmin):
    pass