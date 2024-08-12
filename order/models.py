from django.db import models

class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='лодка')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='электронная почта')
    message = models.TextField(verbose_name='сообщение')

    closed = models.BooleanField(default=False, verbose_name='закрыт')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ на лодку {self.boat} от {self.email}'


    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['-created']

