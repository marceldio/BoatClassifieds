# Generated by Django 5.0.7 on 2024-08-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0009_alter_boat_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='boat/photo', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='name',
            field=models.CharField(max_length=50, verbose_name='названиe'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='год выпуска'),
        ),
    ]