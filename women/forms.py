from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')

class AddGameForm(forms.ModelForm):
    name = forms.CharField(
        label='Название игры',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Game
        fields = ['name',]

class AddSquadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].empty_label = "Игра не выбрана"

    class Meta:
        model = Squad
        fields = ['name', 'game']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            # 'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class AttrForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Player
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            # 'user': forms.HiddenInput()
            # 'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

class AddPlayerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['game'].empty_label = "Игра не выбрана"

    def save(self, user, attr, attr_ch, attr_tt, invent, stats, race):
        obj = super(AddPlayerForm, self).save(commit=False)
        obj.user = user
        # obj.attr = Attr.objects.get(pk=attr)
        obj.attr = attr
        obj.attr_ch = attr_ch
        obj.attr_tt = attr_tt
        # obj.inventory = PlayerInventory.objects.get(pk=invent)
        obj.inventory = invent
        if Race.objects.get(name=race).language:
            obj.language += f',{Race.objects.get(name=race).language}'
        # obj.stats = PlayerStats.objects.get(pk=stats)
        obj.stats = stats
        return obj.save()

    class Meta:
        model = Player
        fields = [
            'name',
            'photo',
            'squadName',
            'Race',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class JoinGame(forms.Form):

    def __init__(self, *args, **kwargs):
        super(JoinGame, self).__init__(*args, **kwargs)
        self.user = self.initial['user']
        getCharacters = Player.objects.filter(user=self.user).exclude(dead=True)
        gameList = []
        for character in getCharacters:
            if character.squadName:
                if character.squadName.game:
                    gameList.append(character.squadName.game.pk)
        self.fields['game'] = forms.ModelChoiceField(
            queryset=Game.objects.filter(pk__in=gameList),
            label='Название игры'
            # initial=0
        )

class CreateMap(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateMap, self).__init__(*args, **kwargs)
        if 'gameId' in self.initial.keys():
            self.gameId = self.initial['gameId']
            self.fields['game'] = forms.ModelChoiceField(
                queryset=Game.objects.filter(pk=self.gameId),
                initial=0,
                label='Название игры',
                # disabled=True,
            )

    class Meta:
        model = Maps
        fields = [
            'name',
            'map',
            # 'slug',
            'game'
        ]