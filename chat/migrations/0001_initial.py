# Generated by Django 3.1.7 on 2021-04-11 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('women', '0061_auto_20210403_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=3000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='women.player')),
            ],
        ),
    ]
