# Generated by Django 3.1.7 on 2021-03-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_auto_20210307_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='squads',
        ),
        migrations.AddField(
            model_name='squad',
            name='game',
            field=models.ForeignKey(limit_choices_to={'complete': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='women.game', verbose_name='Игра'),
        ),
    ]