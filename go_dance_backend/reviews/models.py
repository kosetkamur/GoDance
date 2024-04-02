from django.db import models

from go_dance_backend.user.models import User

from go_dance_backend.organizators.models import Organizator


class Review(models.Model):

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    author = models.CharField(max_length=255)
    date = models.DateField()
    rating = models.FloatField(default=0.0)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
