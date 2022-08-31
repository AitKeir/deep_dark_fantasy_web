# Generated by Django 3.1.7 on 2021-03-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0025_auto_20210308_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enemy',
            options={'ordering': ['name'], 'verbose_name': 'Врага', 'verbose_name_plural': 'Враги'},
        ),
        migrations.AlterField(
            model_name='attr',
            name='periodicTypeDmg',
            field=models.CharField(blank=True, choices=[('poison', 'Яд'), ('bleeding', 'Кровотечение'), ('magic', 'Магия')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Quests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название квеста')),
                ('description', models.TextField(blank=True, verbose_name='Детали')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_quest', to='women.player', verbose_name='Игрок')),
                ('squad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='squad_quest', to='women.squad', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
                'ordering': ['name'],
            },
        ),
    ]