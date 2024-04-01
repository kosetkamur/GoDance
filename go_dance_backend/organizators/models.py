from django.db import models, IntegrityError
from go_dance_backend.user.models import User

from go_dance_backend.styles.models import Style


class Company(models.Model):

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
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

    def save(self, *args, **kwargs):
        if self.teacher_id is not None and self.company_id is not None:
            raise IntegrityError
        return super().save(*args, **kwargs)