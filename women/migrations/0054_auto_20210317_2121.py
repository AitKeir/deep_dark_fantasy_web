# Generated by Django 3.1.7 on 2021-03-17 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0053_auto_20210316_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maps',
            options={'ordering': ['name'], 'verbose_name': 'Карту', 'verbose_name_plural': 'Карты'},
        ),
    ]