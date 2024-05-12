from django.db import models, IntegrityError
from go_dance_backend.user.models import User

from go_dance_backend.styles.models import Style


class Teacher(models.Model):

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512, null=True)
    age = models.IntegerField()
    image = models.FileField(upload_to='photos/')
    experience = models.IntegerField()
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=255, verbose_name="Расписание", null=True)

    def __str__(self):
        return self.name

class Company(models.Model):

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255)
    image = models.FileField(upload_to='photos/')
    schedule = models.CharField(max_length=255, null=True)
    teachers = models.ManyToManyField(Teacher, related_name="groups", through="CompanyTeacher")

    def __str__(self):
        return self.name


class TeacherStyle(models.Model):
    class Meta:
        verbose_name = "Стиль преподавателя"
        verbose_name_plural = "Стили преподавателя"

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher


class CompanyStyle(models.Model):
    class Meta:
        verbose_name = "Стиль преподавателя в школе"
        verbose_name_plural = "Стили преподавателя в школах"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

class CompanyTeacher(models.Model):
    class Meta:
        verbose_name = "Учитель в школе"
        verbose_name_plural = "Учителя в школе"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company} {self.teacher}"


class Organizator(models.Model):
    class Meta:
        verbose_name = "Организатор"
        verbose_name_plural = "Организаторы"

    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)
    vk_ref = models.CharField(max_length=255)
    telegram_ref = models.CharField(max_length=255)

    def __str__(self):
        return str(self.company) or str(self.teacher)

    @property
    def organizator_type(self):
        if self.teacher_id:
            return "teacher"
        return "school"

    @property
    def name(self):
        if self.teacher_id:
            return self.teacher.name
        return self.company.name

    @property
    def schedule(self):
        if self.teacher_id:
            return None
        return self.company.schedule

    @property
    def description(self):
        if self.teacher_id:
            return self.teacher.description
        return self.company.description

    @property
    def image(self):
        if self.teacher_id:
            return self.teacher.image.url if self.teacher.image else ""
        return self.company.image.url if self.company.image else ""

    @property
    def rating(self):
        if self.teacher_id:
            return self.teacher.rating
        return self.company.rating

    @property
    def address(self):
        if self.teacher_id:
            return self.teacher.address
        return self.company.address


    @property
    def teachers(self):
        if self.teacher_id:
            return []

        return Teacher.objects.filter(companyteacher__company_id=self.company_id)

    @property
    def courses(self):
        from ..courses.models import Course

        if self.teacher_id:
            return Course.objects.filter(teacher_id=self.teacher_id, master_class=False)

        return Course.objects.filter(teacher__companyteacher__company_id=self.company_id, master_class=False)

    @property
    def master_classes(self):
        from ..courses.models import Course

        if self.teacher_id:
            return Course.objects.filter(teacher_id=self.teacher_id, master_class=True)

        return Course.objects.filter(teacher__companyteacher__company_id=self.company_id, master_class=True)

    @property
    def events(self):
        from ..events.models import Event

        if self.teacher_id:
            return Event.objects.filter(teacher_id=self.teacher_id)

        return Event.objects.filter(teacher__companyteacher__company_id=self.company_id)

    @property
    def reviews(self):
        from ..reviews.models import Review

        return Review.objects.filter(organizator_id=self.id)

    def save(self, *args, **kwargs):
        if self.teacher_id is not None and self.company_id is not None:
            raise IntegrityError
        return super().save(*args, **kwargs)
