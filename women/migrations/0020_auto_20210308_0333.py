# Generated by Django 3.1.7 on 2021-03-08 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0019_auto_20210308_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip',
            name='attr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equip_attr', to='women.attr', verbose_name='Атрибуты'),
        ),
    ]