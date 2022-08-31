# Generated by Django 3.1.7 on 2021-03-13 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0047_auto_20210314_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Раса')),
            ],
            options={
                'verbose_name': 'Расу противника',
                'verbose_name_plural': 'Расы противника',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='enemy',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_enemy', to='women.enemytype', verbose_name='Раса врага'),
        ),
    ]