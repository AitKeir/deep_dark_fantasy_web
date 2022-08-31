from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'complete', 'id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class SquadAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'magicSchool',)
    list_display_links = ('name',)
    search_fields = ('name', )

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'squadName', 'dead', 'get_html_photo', 'id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = (
        'name',
        'user',
        'photo',
        'get_html_photo',
        'squadName',
        'Race',
        'language',
        'stats',
        'attr',
        'attr_ch',
        'attr_tt',
        'inventory',
        'magicSkill',
        'activeSkill',
        'passiveSkill',
        'magicSchool1',
        'magicSchool2',
        'dead'
    )
    readonly_fields = (
        'get_html_photo',
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Изображение"

class MagicSchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class TypeEquipAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)

class EquipAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class AttrAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_display_links = ('name', 'id',)
    search_fields = ('name', 'id',)
    save_on_top = True
    fields = (
        ('name', 'type_attr'),
        ('energy', 'regenEnergy', 'haste'),
        ('hit', 'dmg', 'arp'),
        ('hp', 'regenHp', 'regenHpDaily'),
        ('evade', 'armor', 'magicArmor'),
        ('magicResist', 'mp', 'regenMp'),
        ('regenMpDaily', 'magicPenetration', 'magicIgnore'),
        ('magicPeriodicDmg', 'poisonPeriodicDmg', 'bleedingPeriodicDmg'),
        ('magicDirDmg', 'stunChance', 'vampiric'),
        'cursed'
    )

class EnemyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_html_photo')
    list_display_links = ('name',)
    search_fields = ('name',)
    fields = (
        'name',
        'photo',
        'get_html_photo',
        'stats',
        'attr',
        'attr_ch',
        'attr_tt',
        'inventory',
        'type'
    )
    readonly_fields = (
        'get_html_photo',
    )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Изображение"

class PlayerInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_display_links = ('name', 'id',)
    search_fields = ('name', 'id',)
    save_on_top = True
    fields = (
        'name',
        'rightHand',
        'leftHand',
        'chest',
        'amulet',
        'ring',
        'book',
        ('gold', 'projectiles'),
        'bag',
    )

class QuestsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class EnemyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)

class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_display_links = ('name', 'id',)
    search_fields = ('name', 'id',)
    save_on_top = True
    fields = (
        'name',
        'freeStatPoints',
        ('meleFightAtt', 'meleFightPlus', 'meleFightDesc'),
        ('shootAtt', 'shootPlus', 'shootDesc'),
        ('slamAtt', 'slamPlus', 'slamDesc'),
        ('armorRateAtt', 'armorRatePlus', 'armorRateDesc'),
        ('tacticAtt', 'tacticPlus', 'tacticDesc'),
        'allInAgi',
        ('hitAtt', 'hitPlus', 'hitDesc'),
        ('dodgeAtt', 'dodgePlus', 'dodgeDesc'),
        ('hasteAtt', 'hastePlus', 'hasteDesc'),
        ('coldBloodAtt', 'coldBloodPlus', 'coldBloodDesc'),
        ('thiefArtAtt', 'thiefArtPlus', 'thiefArtDesc'),
        'allInInt',
        ('manaAtt', 'manaPlus', 'manaDesc'),
        ('firstAidAtt', 'firstAidPlus', 'firstAidDesc'),
        ('circleAtt', 'circlePlus', 'circleDesc'),
        ('magicPowerAtt', 'magicPowerPlus', 'magicPowerDesc'),
        ('learningAtt', 'learningPlus', 'learningDesc'),
        'allInBody',
        ('hpAtt', 'hpPlus', 'hpDesc'),
        ('energyAtt', 'energyPlus', 'energyDesc'),
        ('resistAtt', 'resistPlus', 'resistDesc'),
        ('secondBreathAtt', 'secondBreathPlus', 'secondBreathDesc'),
        ('steelBodyAtt', 'steelBodyPlus', 'steelBodyDesc'),
    )

class DescriptionAllAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)

class MapsAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_html_photo', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)

    fields = (
        'name',
        'slug',
        'get_html_photo',
        'map',
        'game'
    )
    readonly_fields = (
        'get_html_photo',
    )
    prepopulated_fields = {"slug": ("name",)}

    def get_html_photo(self, object):
        if object.map:
            return mark_safe(f"<img src='{object.map.url}' width=50>")

    get_html_photo.short_description = "Изображение"

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(MagicSchool, MagicSchoolAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(TypeEquip, TypeEquipAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(Attr, AttrAdmin)
admin.site.register(PlayerInventory, PlayerInventoryAdmin)
admin.site.register(Enemy, EnemyAdmin)
admin.site.register(Quests, QuestsAdmin)
admin.site.register(EnemyType, EnemyTypeAdmin)
admin.site.register(PlayerStats, PlayerStatsAdmin)
admin.site.register(DescriptionAll, DescriptionAllAdmin)
admin.site.register(Maps, MapsAdmin)
