# Generated by Django 3.1.7 on 2021-03-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0044_auto_20210314_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attr',
            name='armor',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Броня'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='arp',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Пробивание брони'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='bleedingPeriodicDmg',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Периодический урон от кровотечения'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='dmg',
            field=models.CharField(blank=True, default='0/0/0', max_length=255, null=True, verbose_name='Урон'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='energy',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Энергия'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='evade',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Уклонение'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='haste',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Скорость'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='hit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Меткость'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='hp',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicArmor',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Магическая броня'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicDirDmg',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Прямой магический урон'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicIgnore',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Пробивание магической брони'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicPenetration',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Магическое проникновение'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicPeriodicDmg',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Периодический магический урон'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='magicResist',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Магическое сопротивление'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='mp',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Мана'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='poisonPeriodicDmg',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Периодический урон от яда'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='regenEnergy',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Регенерация энергии'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='regenHp',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Регенерация здоровья в бою'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='regenHpDaily',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Дневная регенерация здоровья'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='regenMp',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Регенерация маны в бою'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='regenMpDaily',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Дневная регенрация маны'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='stunChance',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Шанс оглушения'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='vampiric',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Процент вампиризма'),
        ),
    ]
