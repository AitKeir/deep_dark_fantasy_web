# Generated by Django 3.1.7 on 2021-03-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0015_auto_20210307_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='race', to='women.race', verbose_name='Раса'),
        ),
        migrations.AlterField(
            model_name='player',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language', to='women.language', verbose_name='Язык'),
        ),
    ]
