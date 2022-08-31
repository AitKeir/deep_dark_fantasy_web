# Generated by Django 3.1.7 on 2021-03-07 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_auto_20210307_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='passiveSkill',
            field=models.ForeignKey(blank=True, limit_choices_to={'skilltype': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passive_ability', to='women.skillcategory', verbose_name='Пассивное умение'),
        ),
    ]