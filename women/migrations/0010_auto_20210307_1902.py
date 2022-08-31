# Generated by Django 3.1.7 on 2021-03-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_auto_20210307_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='activeSkill',
            field=models.ForeignKey(blank=True, limit_choices_to={'skilltype': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active_ability', to='women.skillcategory', verbose_name='Активное умение'),
        ),
        migrations.AlterField(
            model_name='player',
            name='magicSkill',
            field=models.ForeignKey(blank=True, limit_choices_to={'skilltype': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='magic_ability', to='women.skillcategory', verbose_name='Магическое умение'),
        ),
    ]