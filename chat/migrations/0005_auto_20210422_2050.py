# Generated by Django 3.1.7 on 2021-04-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_ch_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ch_groups',
            name='pers',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
