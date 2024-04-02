from django.db import models

from go_dance_backend.courses.models import Course
from go_dance_backend.organizators.models import Teacher
from go_dance_backend.user.models import User


class Seance(models.Model):

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    time = models.DateTimeField()
    duration = models.IntegerField(verbose_name="Длительность в минутах", default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.time} {self.teacher}"


class UserCourseBooking(models.Model):
    class Meta:
        verbose_name = "Запись на курс"
        verbose_name_plural = "Записи на курсы"

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} {self.user}"

    @property
    def name(self):
        return self.course.name

    @property
    def style(self):
        return self.course.style.name

    @property
    def duration(self):
        return self.course.duration


class Booking(models.Model):

    class Meta:
        verbose_name = "Запись на мастеркласс"
        verbose_name_plural = "Записи на мастерклассы"

    seance = models.ForeignKey(Seance, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seance} {self.user}"

    @property
    def duration(self):
        return self.seance.duration

    @property
    def time(self):
        return self.seance.time
