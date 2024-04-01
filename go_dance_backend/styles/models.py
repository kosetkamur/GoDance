from django.db import models

class Style(models.Model):

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name