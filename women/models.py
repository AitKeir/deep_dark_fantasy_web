import null as null
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Game(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название игры"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
        blank=True
    )
    complete = models.BooleanField(
        default=False,
        verbose_name="Завершена"
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'
        ordering = ['-id']

class Squad(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название команды"
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.SET_NULL,
        verbose_name="Игра",
        null=True,
        blank=True,
        limit_choices_to = {'complete': False}
    )
    # players = models.CharField(
    #     max_length=255,
    #     verbose_name="Персонажи",
    #     blank=True
    # )
    days = models.CharField(
        max_length=255,
        verbose_name="Дней в игре",
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'
        ordering = ['id']

class Player(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя персонажа"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        blank=True
    )
    photo = models.ImageField(
        upload_to="players/%Y/%m/%d/",
        verbose_name="Изображение",
        # default="players/default.png"
    )
    squadName = models.ForeignKey(
        'Squad',
        on_delete=models.SET_NULL,
        verbose_name="Команда",
        related_name="squad",
        null=True,
        blank=True,
    )
    Race = models.ForeignKey(
        'Race',
        on_delete=models.SET_NULL,
        verbose_name="Раса",
        related_name="race",
        null=True,
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Язык",
        default='Общий',
        blank=True,
    )
    stats = models.ForeignKey(
        'PlayerStats',
        on_delete=models.CASCADE,
        verbose_name="Характеристики",
        related_name="Player_Stats",
        null=True,
        blank=True,
    )
    attr = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Атрибуты",
        related_name="Attr_player",
        null=True,
        blank=True,
    )
    attr_ch = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Временные атрибуты",
        related_name="Attr_player_ch",
        null=True,
        blank=True,
    )
    attr_tt = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Итоговые атрибуты",
        related_name="Attr_player_tt",
        null=True,
        blank=True,
    )
    inventory = models.ForeignKey(
        'PlayerInventory',
        on_delete=models.CASCADE,
        verbose_name="Инвентарь",
        related_name="inventory_player",
        null=True,
        blank=True,
    )
    magicSkill = models.ForeignKey(
        'SkillCategory',
        on_delete=models.SET_NULL,
        verbose_name="Магическое умение",
        related_name="magic_ability",
        null=True,
        blank=True,
        limit_choices_to={'skilltype': 1}
    )
    activeSkill = models.ForeignKey(
        'SkillCategory',
        on_delete=models.SET_NULL,
        verbose_name="Активное умение",
        related_name="active_ability",
        null=True,
        blank=True,
        limit_choices_to = {'skilltype': 3}
    )
    passiveSkill = models.ForeignKey(
        'SkillCategory',
        on_delete=models.SET_NULL,
        verbose_name="Пассивное умение",
        related_name="passive_ability",
        null=True,
        blank=True,
        limit_choices_to={'skilltype': 2}
    )
    magicSchool1 = models.ForeignKey(
        'MagicSchool',
        on_delete=models.SET_NULL,
        verbose_name="Магическая школа 1",
        related_name="magic_school_1",
        null=True,
        blank=True,
    )
    magicSchool2 = models.ForeignKey(
        'MagicSchool',
        on_delete=models.SET_NULL,
        verbose_name="Магическая школа 2",
        related_name="magic_school_2",
        null=True,
        blank=True,
    )

    dead = models.BooleanField(
        default=False,
        verbose_name="Мертв"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонажа'
        verbose_name_plural = 'Персонажи'
        ordering = ['id']

class SkillCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя скила"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Текст статьи"
    )
    skilltype = models.ForeignKey(
        'SkillType',
        on_delete=models.PROTECT,
        verbose_name="Тип способности",
    )
    magicSchool = models.ForeignKey(
        'MagicSchool',
        on_delete=models.SET_NULL,
        verbose_name="Магическая школа",
        related_name="magic_school",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скил'
        verbose_name_plural = 'Скилы'
        ordering = ['name']

class SkillType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя типа способности"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип скила'
        verbose_name_plural = 'Типы скилов'
        ordering = ['name']

class MagicSchool(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя школы магии"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школу магии'
        verbose_name_plural = 'Школы магии'
        ordering = ['name']

class Race(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Раса"
    )
    description = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание расы",
        related_name="description_race",
        null=True,
        blank=True,
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.SET_NULL,
        verbose_name="Язык",
        related_name="language",
        null=True,
        blank=True,
    )
    startlvl = models.IntegerField(
        null=True,
        blank=True,
        default=1,
        verbose_name="Стартовая уровень"
    )
    startStr = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стартовая сила"
    )
    startAgi = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стартовая ловкость"
    )
    startInt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стартовый интелект"
    )
    startBody = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стартовое телосложение"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расу'
        verbose_name_plural = 'Расы'
        ordering = ['name']

class Language(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Раса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['name']

class Equip(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    attr = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Атрибуты",
        related_name="equip_attr",
    )
    typeEquip = models.ForeignKey(
        'TypeEquip',
        on_delete=models.PROTECT,
        verbose_name="Тип экипировки",
        related_name="type_equip",
    )
    lvl = models.IntegerField(
        verbose_name="Уровень"
    )
    handType = models.BooleanField(
        default=False,
        verbose_name="Двуручное"
    )
    rangeType = models.BooleanField(
        default=False,
        verbose_name="Дальнобойное"
    )
    cost = models.IntegerField(
        verbose_name="Цена"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент экипировки'
        verbose_name_plural = 'Экипировка'
        ordering = ['name']

class Attr(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Чьи атрибуты",
        default='Нет'
    )
    energy = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Энергия"
    )
    regenEnergy = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Регенерация энергии"
    )
    haste = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Скорость"
    )
    hit = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Меткость"
    )
    dmg = models.CharField(
        max_length=25,
        verbose_name="Урон",
        null=True,
        blank=True,
        default='0/0/0',
    )
    arp = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Пробивание брони"
    )
    hp = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Здоровье"
    )
    regenHp = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Регенерация здоровья в бою"
    )
    regenHpDaily = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Дневная регенерация здоровья"
    )
    evade = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Уклонение"
    )
    armor = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Броня"
    )
    magicArmor = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Магическая броня"
    )
    magicResist = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Магическое сопротивление"
    )
    mp = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Мана"
    )
    regenMp = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Регенерация маны в бою"
    )
    regenMpDaily = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Дневная регенрация маны"
    )
    magicPenetration = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Магическое проникновение"
    )
    magicIgnore = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Пробивание магической брони"
    )
    magicDirDmg = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Прямой магический урон"
    )
    magicPeriodicDmg = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Периодический магический урон"
    )
    poisonPeriodicDmg = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Периодический урон от яда"
    )
    bleedingPeriodicDmg = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Периодический урон от кровотечения"
    )
    stunChance = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Шанс оглушения"
    )
    vampiric = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Процент вампиризма"
    )
    cursed = models.BooleanField(
        default=False,
        verbose_name="Проклят"
    )
    type_attr = models.CharField(
        max_length=2,
        choices=[('st', 'static'), ('ch', 'change'), ('tt', 'total')],
        default='st',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'
        # ordering = ['name']

class TypeEquip(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Тип экипировки"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип экипировки'
        verbose_name_plural = 'Типы экипировки'
        ordering = ['name']

class PlayerInventory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Чей инвентарь",
        default='Нет',
        # null=True,
        # blank=True,
    )
    rightHand = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Правая рука",
        related_name="right_hand",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 2}
    )
    leftHand = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Левая рука",
        related_name="left_hand",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 2, 'typeEquip': 1}
    )
    chest = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Броня",
        related_name="chest_armor",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 3}
    )
    amulet = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Амулет",
        related_name="amulet_player",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 4}
    )
    ring = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Кольцо",
        related_name="ring_player",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 5}
    )
    book = models.ForeignKey(
        'Equip',
        on_delete=models.SET_NULL,
        verbose_name="Книга",
        related_name="book_player",
        null=True,
        blank=True,
        limit_choices_to={'typeEquip': 6}
    )
    gold = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Золото"
    )
    projectiles = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Снаряды"
    )
    bag = models.TextField(
        blank=True,
        verbose_name="Сумка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентари'
        # ordering = ['name']

class Enemy(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    photo = models.ImageField(
        upload_to="enemies/%Y/%m/%d/",
        verbose_name="Изображение",
        default="enemies/default.jpg"
    )
    stats = models.ForeignKey(
        'PlayerStats',
        on_delete=models.CASCADE,
        verbose_name="Характеристики",
        related_name="Enemy_Stats",
        null=True,
        blank=True,
    )
    attr = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Атрибуты",
        related_name="Attr_enemy",
        null=True,
        blank=True,
    )
    attr_ch = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Временные атрибуты",
        related_name="Attr_enemy_ch",
        null=True,
        blank=True,
    )
    attr_tt = models.ForeignKey(
        'Attr',
        on_delete=models.CASCADE,
        verbose_name="Итоговые атрибуты",
        related_name="Attr_enemy_tt",
        null=True,
        blank=True,
    )
    inventory = models.ForeignKey(
        'PlayerInventory',
        on_delete=models.CASCADE,
        verbose_name="Инвентарь",
        related_name="inventory_enemy",
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        'EnemyType',
        on_delete=models.SET_NULL,
        verbose_name="Раса врага",
        related_name="type_enemy",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врага'
        verbose_name_plural = 'Враги'
        ordering = ['name']

class Quests(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название квеста"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Детали"
    )
    squad = models.ForeignKey(
        'Squad',
        on_delete=models.SET_NULL,
        verbose_name="Команда",
        related_name="squad_quest",
        null=True,
        blank=True,
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.SET_NULL,
        verbose_name="Игрок",
        related_name="player_quest",
        null=True,
        blank=True,
    )
    complete = models.BooleanField(
        default=False,
        verbose_name="Завершен"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'
        ordering = ['name']

class EnemyType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Раса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расу противника'
        verbose_name_plural = 'Расы противника'
        ordering = ['name']

class PlayerStats(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Чьи характеристики"
    )
    freeStatPoints = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Свободные очки характеристик"
    )
    # str
    allInSTR = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Всего вложено в силу"
    )
    meleFightAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Ближний бой"
    )
    meleFightPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Ближний бой доп"
    )
    meleFightDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание ближнего боя",
        related_name="meleFightDesc",
        null=True,
        blank=True,
    )
    shootAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стрельба"
    )
    shootPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стрельба доп"
    )
    shootDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание стрельбы",
        related_name="shootDesc",
        null=True,
        blank=True,
    )
    slamAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Мощные удары"
    )
    slamPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Мощные удары доп"
    )
    slamDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание мощных ударов",
        related_name="slamDesc",
        null=True,
        blank=True,
    )
    armorRateAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Ратное дело"
    )
    armorRatePlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Ратное дело доп"
    )
    armorRateDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание ратного дела",
        related_name="armorRateDesc",
        null=True,
        blank=True,
    )
    tacticAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Тактика"
    )
    tacticPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Тактика доп"
    )
    tacticDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание тактики",
        related_name="tacticDesc",
        null=True,
        blank=True,
    )
    # agi
    allInAgi = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Всего вложено в ловкость"
    )
    hitAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Меткость"
    )
    hitPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Меткость доп"
    )
    hitDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание меткости",
        related_name="hitDesc",
        null=True,
        blank=True,
    )
    dodgeAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Уклонение"
    )
    dodgePlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Уклонение доп"
    )
    dodgeDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание уклонения",
        related_name="dodgeDesc",
        null=True,
        blank=True,
    )
    hasteAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Скорость"
    )
    hastePlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Скорость доп"
    )
    hasteDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание скорости",
        related_name="hasteDesc",
        null=True,
        blank=True,
    )
    coldBloodAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Хладнокровие"
    )
    coldBloodPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Хладнокровие доп"
    )
    coldBloodDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание хладнокровия",
        related_name="coldBloodDesc",
        null=True,
        blank=True,
    )
    thiefArtAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Воровское дело"
    )
    thiefArtPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Воровское дело доп"
    )
    thiefArtDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание воровского дела",
        related_name="thiefArtDesc",
        null=True,
        blank=True,
    )
    # int
    allInInt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Всего вложено в интелект"
    )
    manaAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Мана"
    )
    manaPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Мана доп"
    )
    manaDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание маны",
        related_name="manaDesc",
        null=True,
        blank=True,
    )
    firstAidAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Первая помощь"
    )
    firstAidPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Первая помощь доп"
    )
    firstAidDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание первой помощи",
        related_name="firstAidDesc",
        null=True,
        blank=True,
    )
    circleAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Круги магии"
    )
    circlePlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Круги магии доп"
    )
    circleDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание кругов магии",
        related_name="circleDesc",
        null=True,
        blank=True,
    )
    magicPowerAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Сила магии"
    )
    magicPowerPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Сила магии доп"
    )
    magicPowerDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание силы магии",
        related_name="magicPowerDesc",
        null=True,
        blank=True,
    )
    learningAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Обучаемость"
    )
    learningPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Обучаемость доп"
    )
    learningDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание обучаемости",
        related_name="learningDesc",
        null=True,
        blank=True,
    )
    # body
    allInBody = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Всего вложено в телосложение"
    )
    hpAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Здоровье"
    )
    hpPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Здоровье доп"
    )
    hpDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание здоровья",
        related_name="hpDesc",
        null=True,
        blank=True,
    )
    energyAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Энергия"
    )
    energyPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Энергия доп"
    )
    energyDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание энергии",
        related_name="energyDesc",
        null=True,
        blank=True,
    )
    resistAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Сопротивляемость"
    )
    resistPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Сопротивляемость доп"
    )
    resistDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание сопротивляемости",
        related_name="resistDesc",
        null=True,
        blank=True,
    )
    secondBreathAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Второе дыхание"
    )
    secondBreathPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Второе дыхание доп"
    )
    secondBreathDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание второго дыхания",
        related_name="secondBreathDesc",
        null=True,
        blank=True,
    )
    steelBodyAtt = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стальное тело"
    )
    steelBodyPlus = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Стальное тело доп"
    )
    steelBodyDesc = models.ForeignKey(
        'DescriptionAll',
        on_delete=models.SET_NULL,
        verbose_name="Описание стального тела",
        related_name="steelBodyDesc",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Набор зарактеристик'
        verbose_name_plural = 'Наборы характеристик'
        ordering = ['name']

class DescriptionAll(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Чье описание"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'
        ordering = ['name']

class Maps(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название местности"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
        blank=True,
    )
    map = models.ImageField(
        upload_to="maps/%Y/%m/%d/",
        verbose_name="Карта",
        blank=True,
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.SET_NULL,
        verbose_name="Игра",
        null=True,
        blank=True,
        limit_choices_to={'complete': False}
    )

    def get_absolute_url(self):
        return reverse('maps', kwargs={'maps_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карту'
        verbose_name_plural = 'Карты'
        ordering = ['name']