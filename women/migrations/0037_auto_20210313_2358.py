# Generated by Django 3.1.7 on 2021-03-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0036_auto_20210313_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='language',
            field=models.CharField(blank=True, default='Общий', max_length=255, verbose_name='Язык'),
        ),
    ]
