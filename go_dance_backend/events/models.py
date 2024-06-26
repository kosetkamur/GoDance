from django.db import models

from go_dance_backend.organizators.models import Teacher, Organizator
from go_dance_backend.styles.models import Style


class Event(models.Model):

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255, verbose_name="Длительность мероприятия")
    date = models.DateField()
    address = models.CharField(max_length=255)
    count_people = models.IntegerField()
    price = models.CharField(max_length=255)
    present = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    image = models.FileField(upload_to='event_images/')

    def __str__(self):
        return self.name


class OrganizatorEvent(models.Model):
    class Meta:
        verbose_name = "Мероприятие организатора"
        verbose_name_plural = "Мероприятия организаторов"

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)
