# Generated by Django 3.1.7 on 2021-03-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0024_player_squadname'),
    ]

    operations = [
        migrations.AddField(
            model_name='attr',
            name='periodicDmg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Периодический урон'),
        ),
        migrations.AddField(
            model_name='attr',
            name='periodicTypeDmg',
            field=models.CharField(blank=True, choices=[('poison', 'poison'), ('bleeding', 'bleeding'), ('magic', 'magic')], max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('attr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Attr_enemy', to='women.attr', verbose_name='Атрибуты')),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory_enemy', to='women.playerinventory', verbose_name='Инвентарь')),
            ],
        ),
    ]
