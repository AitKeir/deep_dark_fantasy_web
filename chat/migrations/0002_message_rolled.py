# Generated by Django 3.1.7 on 2021-04-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='rolled',
            field=models.BooleanField(default=False),
        ),
    ]
