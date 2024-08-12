import datetime

from django.db import models

from boat.models import Owner, Boat

NULLABLE = {'blank': True, 'null': True}


class Offer(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='offer')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец')
    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='обновлено')

    def is_active(self):
        return self.created_at.date() <= datetime.now().date()

    def __str__(self):
        return f'{self.boat} ({self.owner})'

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
