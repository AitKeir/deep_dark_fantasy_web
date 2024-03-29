# Generated by Django 3.1.7 on 2021-03-07 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_auto_20210307_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя типа способности')),
            ],
        ),
        migrations.AlterField(
            model_name='squad',
            name='days',
            field=models.CharField(blank=True, max_length=255, verbose_name='Дней в игре'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='game',
            field=models.ForeignKey(blank=True, limit_choices_to={'complete': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='women.game', verbose_name='Игра'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='players',
            field=models.CharField(blank=True, max_length=255, verbose_name='Персонажи'),
        ),
        migrations.CreateModel(
            name='skillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя скила')),
                ('description', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('skilltype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.skill_type', verbose_name='Тип способности')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя персонажа')),
                ('attr', models.CharField(blank=True, max_length=255, verbose_name='Характеристики')),
                ('magicSkill', models.ForeignKey(blank=True, limit_choices_to={'skilltype': 'magic'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='women.skillcategory', verbose_name='Магическое умение')),
            ],
        ),
    ]
