# Generated by Django 3.1.7 on 2021-03-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0032_auto_20210310_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default='2021-03-07 10:21:14.359622-05', verbose_name='Время создания'),
            preserve_default=False,
        ),
    ]