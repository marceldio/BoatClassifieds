# Generated by Django 5.0.7 on 2024-08-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0008_alter_boat_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='опубликовано'),
        ),
    ]