# Generated by Django 3.1.7 on 2021-03-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0048_auto_20210314_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Чье описание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описания',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='race',
            name='startAgi',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Стартовая ловкость'),
        ),
        migrations.AddField(
            model_name='race',
            name='startBody',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Стартовое телосложение'),
        ),
        migrations.AddField(
            model_name='race',
            name='startInt',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Стартовый интелект'),
        ),
        migrations.AddField(
            model_name='race',
            name='startStr',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Стартовая сила'),
        ),
        migrations.AlterField(
            model_name='race',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language', to='women.language', verbose_name='Язык'),
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Чьи характеристики')),
                ('freeStatPoints', models.IntegerField(blank=True, default=0, null=True, verbose_name='Свободные очки характеристик')),
                ('allInSTR', models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего вложено в силу')),
                ('meleFightAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ближний бой')),
                ('meleFightPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ближний бой доп')),
                ('shootAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Стрельба')),
                ('shootPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Стрельба доп')),
                ('slamAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Мощные удары')),
                ('slamPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Мощные удары доп')),
                ('armorRateAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ратное дело')),
                ('armorRatePlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ратное дело доп')),
                ('tacticAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Тактика')),
                ('tacticPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Тактика доп')),
                ('allInAgi', models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего вложено в ловкость')),
                ('hitAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Меткость')),
                ('hitPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Меткость доп')),
                ('dodgeAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Уклонение')),
                ('dodgePlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Уклонение доп')),
                ('hasteAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скорость')),
                ('hastePlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скорость доп')),
                ('coldBloodAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Хладнокровие')),
                ('coldBloodPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Хладнокровие доп')),
                ('thiefArtAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Воровское дело')),
                ('thiefArtPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Воровское дело доп')),
                ('allInInt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего вложено в интелект')),
                ('manaAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Мана')),
                ('manaPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Мана доп')),
                ('firstAidAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Первая помощь')),
                ('firstAidPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Первая помощь доп')),
                ('circleAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Круги магии')),
                ('circlePlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Круги магии доп')),
                ('magicPowerAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Сила магии')),
                ('magicPowerPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Сила магии доп')),
                ('learningAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Обучаемость')),
                ('learningPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Обучаемость доп')),
                ('allInBody', models.IntegerField(blank=True, default=0, null=True, verbose_name='Всего вложено в телосложение')),
                ('hpAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Здоровье')),
                ('hpPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Здоровье доп')),
                ('energyAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Энергия')),
                ('energyPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Энергия доп')),
                ('resistAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Сопротивляемость')),
                ('resistPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Сопротивляемость доп')),
                ('secondBreathAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Второе дыхание')),
                ('secondBreathPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Второе дыхание доп')),
                ('steelBodyAtt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Стальное тело')),
                ('steelBodyPlus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Стальное тело доп')),
                ('armorRateDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='armorRateDesc', to='women.descriptionall', verbose_name='Описание ратного дела')),
                ('circleDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='circleDesc', to='women.descriptionall', verbose_name='Описание кругов магии')),
                ('coldBloodDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coldBloodDesc', to='women.descriptionall', verbose_name='Описание хладнокровия')),
                ('dodgeDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dodgeDesc', to='women.descriptionall', verbose_name='Описание уклонения')),
                ('energyDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='energyDesc', to='women.descriptionall', verbose_name='Описание энергии')),
                ('firstAidDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='firstAidDesc', to='women.descriptionall', verbose_name='Описание первой помощи')),
                ('hasteDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hasteDesc', to='women.descriptionall', verbose_name='Описание скорости')),
                ('hitDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hitDesc', to='women.descriptionall', verbose_name='Описание меткости')),
                ('hpDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hpDesc', to='women.descriptionall', verbose_name='Описание здоровья')),
                ('learningDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='learningDesc', to='women.descriptionall', verbose_name='Описание обучаемости')),
                ('magicPowerDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='magicPowerDesc', to='women.descriptionall', verbose_name='Описание силы магии')),
                ('manaDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manaDesc', to='women.descriptionall', verbose_name='Описание маны')),
                ('meleFightDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meleFightDesc', to='women.descriptionall', verbose_name='Описание ближнего боя')),
                ('resistDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resistDesc', to='women.descriptionall', verbose_name='Описание сопротивляемости')),
                ('secondBreathDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondBreathDesc', to='women.descriptionall', verbose_name='Описание второго дыхания')),
                ('shootDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shootDesc', to='women.descriptionall', verbose_name='Описание стрельбы')),
                ('slamDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slamDesc', to='women.descriptionall', verbose_name='Описание мощных ударов')),
                ('steelBodyDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='steelBodyDesc', to='women.descriptionall', verbose_name='Описание стального тела')),
                ('tacticDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tacticDesc', to='women.descriptionall', verbose_name='Описание тактики')),
                ('thiefArtDesc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thiefArtDesc', to='women.descriptionall', verbose_name='Описание воровского дела')),
            ],
            options={
                'verbose_name': 'Набор зарактеристик',
                'verbose_name_plural': 'Наборы характеристик',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='description_race', to='women.descriptionall', verbose_name='Описание расы'),
        ),
    ]