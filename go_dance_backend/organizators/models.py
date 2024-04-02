from django.db import models, IntegrityError
from go_dance_backend.user.models import User

from go_dance_backend.styles.models import Style


class Company(models.Model):

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255)
    image = models.FileField(upload_to='photos/')
    schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    photo = models.FileField(upload_to='photos/')
    experience = models.IntegerField()
    rating = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, null=True)
    image = models.FileField(upload_to='photos/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
        verbose_name = "Стиль преподавателя в шкоел"
        verbose_name_plural = "Стили преподавателя в школах"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    def __str__(self):
        return self.company


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
    def name(self):
        if self.teacher_id:
            return self.teacher.name
        return self.company.name

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

    def save(self, *args, **kwargs):
        if self.teacher_id is not None and self.company_id is not None:
            raise IntegrityError
        return super().save(*args, **kwargs)