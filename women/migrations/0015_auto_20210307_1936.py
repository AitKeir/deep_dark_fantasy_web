# Generated by Django 3.1.7 on 2021-03-07 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0014_auto_20210307_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='game',
            new_name='language',
        ),
    ]