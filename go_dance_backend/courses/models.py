from django.db import models

from go_dance_backend.organizators.models import Teacher
from go_dance_backend.styles.models import Style

class Course(models.Model):

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(verbose_name="Длительность в минутах")
    date = models.DateField()
    address = models.CharField(max_length=255)
    count_people = models.IntegerField()
    shooting = models.CharField(max_length=255)
    music = models.CharField(max_length=255)
    age_restrictions = models.CharField(max_length=255)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    image = models.FileField(upload_to='data_images/')
    master_class = models.BooleanField()

    def __str__(self):
        return self.name