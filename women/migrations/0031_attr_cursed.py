# Generated by Django 3.1.7 on 2021-03-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0030_auto_20210310_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='attr',
            name='cursed',
            field=models.BooleanField(default=False, verbose_name='Проклят'),
        ),
    ]
