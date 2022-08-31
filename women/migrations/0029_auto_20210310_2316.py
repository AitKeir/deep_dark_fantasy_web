# Generated by Django 3.1.7 on 2021-03-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0028_auto_20210309_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attr',
            name='periodicDmg',
        ),
        migrations.RemoveField(
            model_name='attr',
            name='periodicTypeDmg',
        ),
        migrations.AddField(
            model_name='attr',
            name='bleedingPeriodicDmg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Периодический урон от кровотечения'),
        ),
        migrations.AddField(
            model_name='attr',
            name='poisonPeriodicDmg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Периодический урон от яда'),
        ),
    ]
