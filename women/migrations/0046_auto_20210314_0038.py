# Generated by Django 3.1.7 on 2021-03-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0045_auto_20210314_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attr',
            name='dmg',
            field=models.CharField(blank=True, default='0/0/0', max_length=25, null=True, verbose_name='Урон'),
        ),
    ]
