# Generated by Django 3.1.7 on 2021-04-02 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0060_auto_20210403_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
