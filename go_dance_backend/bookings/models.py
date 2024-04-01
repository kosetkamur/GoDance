from django.db import models

class Booking(models.Model):

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company) or str(self.teacher)
