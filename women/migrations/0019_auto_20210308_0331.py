# Generated by Django 3.1.7 on 2021-03-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0018_equip_rangetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeequip',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Тип экипировки'),
        ),
    ]
