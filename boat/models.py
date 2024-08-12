from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='электронная почта', unique=True)
    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name='названиe')
    year = models.PositiveIntegerField(**NULLABLE, verbose_name='год выпуска')
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image = models.ImageField(**NULLABLE,
        upload_to="boat/photo", verbose_name="Изображение")

    price = models.IntegerField(**NULLABLE, verbose_name='цена', default=None)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец')

    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True)

    views_counter = models.PositiveIntegerField(default=0, verbose_name='просмотры',  editable=False)

    is_published = models.BooleanField(default=False, verbose_name="опубликовано")


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'лодка'
        verbose_name_plural = 'лодки'


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    start_year = models.PositiveIntegerField(**NULLABLE, verbose_name='с')
    stop_year = models.PositiveIntegerField(**NULLABLE, verbose_name='по')

    def __str__(self):
        return f'{self.boat} ({self.start_year} - {self.stop_year})'

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'история'


class Version(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
