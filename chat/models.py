from django.db import models
from django.contrib.auth.models import User
from women.models import Player

class Message(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True
    )
    type = models.CharField(
        max_length=255
    )
    rolled = models.BooleanField(
        default=False
    )
    message = models.TextField(
        max_length=3000
    )
    strRoll = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    sumRoll = models.IntegerField(
        null=True,
        blank=True,
    )
    plusRoll = models.IntegerField(
        null=True,
        blank=True,
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to="players/%Y/%m/%d/",
        verbose_name="Изображение",
        # default="players/default.png"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя персонажа"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """
        Строка для представления сообщения
        """

        return self.message

class Ch_groups(models.Model):
    name = models.CharField(
        max_length=255
    )
    pers = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
    )