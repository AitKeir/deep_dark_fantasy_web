# Generated by Django 3.1.7 on 2021-04-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0061_auto_20210403_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='attr',
            name='type_attr',
            field=models.CharField(choices=[('st', 'static'), ('ch', 'change'), ('tt', 'total')], default='st', max_length=2),
        ),
    ]
