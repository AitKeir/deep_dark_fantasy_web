# Generated by Django 3.1.7 on 2021-03-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0011_player_passiveskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagicSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя школы магии')),
            ],
            options={
                'verbose_name': 'Школу магии',
                'verbose_name_plural': 'Школы магии',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['id'], 'verbose_name': 'Игру', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['id'], 'verbose_name': 'Персонажа', 'verbose_name_plural': 'Персонажи'},
        ),
        migrations.AlterModelOptions(
            name='skillcategory',
            options={'ordering': ['name'], 'verbose_name': 'Скил', 'verbose_name_plural': 'Скилы'},
        ),
        migrations.AlterModelOptions(
            name='skilltype',
            options={'ordering': ['name'], 'verbose_name': 'Тип скила', 'verbose_name_plural': 'Типы скилов'},
        ),
        migrations.AlterModelOptions(
            name='squad',
            options={'ordering': ['id'], 'verbose_name': 'Команду', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AddField(
            model_name='player',
            name='magicSchool1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='magic_school_1', to='women.magicschool', verbose_name='Магическая школа 1'),
        ),
        migrations.AddField(
            model_name='player',
            name='magicSchool2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='magic_school_2', to='women.magicschool', verbose_name='Магическая школа 2'),
        ),
    ]
