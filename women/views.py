import re

from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from slugify import slugify

from .forms import *
from chat.views import *
from .models import *
from .utils import *

class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'women/index.html', context=context)

def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

# def login(request):
#     return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'women/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

# @login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        else:
            pass
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'women/profile.html', {
        'menu': menu,
        'user_form': user_form,
        'title': 'Профиль пользователя'
    })

class UpdateProfile(LoginRequiredMixin, DataMixin, CreateView):
    form_class = UserForm
    template_name = 'women/profile.html'
    success_url = reverse_lazy('profile')
    login_url = reverse_lazy('profile')
    raise_exception = True

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Добавление статьи")
    #     return dict(list(context.items()) + list(c_def.items()))

@login_required
def add_game_view(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(form.cleaned_data.get('name'), to_lower=True)
            post.save()
            return redirect('add_game')
    else:
        form = AddGameForm()
    context = {
        'posts': Game.objects.all().order_by('-pk'),
        'form': form,
        'menu': menu,
        'title': 'Добавление игры'
    }
    return render(request, 'women/addgame.html', context)

class AddSquad(LoginRequiredMixin, DataMixin, CreateView, ListView):
    form_class = AddSquadForm
    template_name = 'women/addsquad.html'
    success_url = reverse_lazy('add_squad')
    login_url = reverse_lazy('add_squad')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление команды")
        return dict(list(context.items()) + list(c_def.items()))

    model = Squad
    context_object_name = 'posts'

    def get_queryset(self):
        return Squad.objects.all().order_by('-pk')

class AddPlayer(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPlayerForm
    template_name = 'women/addplayer.html'
    success_url = reverse_lazy('profile')
    login_url = reverse_lazy('profile')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление персонажа")
        return dict(list(context.items()) + list(c_def.items()))

@login_required
def item_desc_view(request):
    # В комментах предзаполнение полей
    # item = get_object_or_404(Player)
    if request.method == 'POST':
        form = AddPlayerForm(request.POST or None, request.FILES)
        formAttr = Attr.objects.get(pk=14)
        formInven = PlayerInventory.objects.get(pk=2)
        formStats = PlayerStats.objects.get(pk=1)
        if form.is_valid():
            nameAll = form.cleaned_data.get('name')
            formAttr.pk = None
            formAttr.name = nameAll
            if form.cleaned_data.get('Race').name == 'Человек':
                formStats.learningPlus += 1
            elif form.cleaned_data.get('Race').name == 'Лесной Эльф':
                formStats.shootPlus += 1
            elif form.cleaned_data.get('Race').name == 'Гном':
                formAttr.magicResist += 1
                formAttr.magicArmor += 1
            formAttr_ch = Attr.objects.create(
                name=f'{nameAll}_ch',
                type_attr='ch'
            )
            formAttr_tt = Attr.objects.create(
                name=f'{nameAll}_tt',
                type_attr='tt',
                energy=formAttr.energy,
                hp=formAttr.hp,
                mp=formAttr.mp,
                magicResist=formAttr.magicResist,
                magicArmor=formAttr.magicArmor,
            )
            formInven.pk = None
            formInven.name = nameAll
            formStats.pk = None
            formStats.name = nameAll
            formAttr.save()
            formInven.save()
            formStats.save()
            # form.save(request.user, formAttr.pk, formAttr_ch.pk, formAttr_tt.pk, formInven.pk, formStats.pk, form.cleaned_data.get('Race'))
            form.save(
                request.user,
                formAttr,
                formAttr_ch,
                formAttr_tt,
                formInven,
                formStats,
                form.cleaned_data.get('Race')
            )
            return redirect('profile')
    else:
        # form = AddPlayerForm(instance=item)
        form = AddPlayerForm()
    # context = {'item': item, 'form': form, }
    return render(request, 'women/addplayer.html', {
        'menu': menu,
        'form': form,
        'title': 'Создание пресонажа'
    })

@login_required
def join_game_view(request):
    getCharacters = Player.objects.filter(user=request.user).exclude(dead=True)
    gameList = []
    for character in getCharacters:
        if character.squadName:
            if character.squadName.game:
                gameList.append(character.squadName.game.pk)
    games = Game.objects.filter(pk__in=gameList)
    context = {
        'games': games,
        'menu': menu,
        'title': 'Выберите игру'
    }
    return render(request, 'women/joingame.html', context)

class ShowGame(DataMixin, DetailView):
    model = Game
    template_name = 'women/show_game.html'
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['game'])
        maps = Maps.objects.filter(game=context['game'].pk)
        listMaps = [('maps', maps)]
        return dict(list(context.items()) + list(c_def.items()) + listMaps)

def save_map(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            mapPhoto = form.save(commit=False)
            mapPhoto.slug = slugify(form.cleaned_data['name'], to_lower=True)
            mapPhoto.save()
            data = {
                'form_is_valid': True,
                'namePhoto': mapPhoto.map.name,
                'urlPhoto': mapPhoto.map.url
            }
            maps = Maps.objects.filter(game_id=form.instance.game_id)
            data['html_book_list'] = render_to_string('women/includes/partial_map_list.html', {
                'maps': maps
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                 context,
                                 request=request,
                                 )
    return JsonResponse(data)

def create_map(request, pk):
    if request.method == 'POST':
        form = CreateMap(request.POST, request.FILES)
    else:
        form = CreateMap(initial={'gameId': pk})
    return save_map(request, form, 'women/includes/partial_map_create.html')

def map_update(request, pk):
    map = get_object_or_404(Maps, pk=pk)
    # get_object_or_404(Game, pk=c_game_id)
    if request.method == 'POST':
        form = CreateMap(request.POST, request.FILES, instance=map)
    else:
        # form = CreateMap(instance=map, initial={'gameId': c_game_id})
        form = CreateMap(instance=map, initial={'gameId': map.game_id})
    return save_map(request, form, 'women/includes/partial_map_update.html')

def map_delete(request, pk):
    map = get_object_or_404(Maps, pk=pk)
    data = dict()
    if request.method == 'POST':
        maps = Maps.objects.filter(game_id=map.game_id)
        map.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        data['html_book_list'] = render_to_string('women/includes/partial_map_list.html', {
            'maps': maps
        })
    else:
        context = {'map': map}
        data['html_form'] = render_to_string('women/includes/partial_map_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


class ShowMap(DataMixin, DetailView):
    model = Maps
    template_name = 'women/show_map.html'
    slug_url_kwarg = 'maps_slug'
    context_object_name = 'maps'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['maps'])
        return dict(list(context.items()) + list(c_def.items()))

def mapShow(request, game_slug, maps_slug):
    messageHistory = Message.objects.filter(type=f"{game_slug}_{maps_slug}")
    map = Maps.objects.get(slug=maps_slug)
    player_now = 0
    for squad in map.game.squad_set.all():
        for player in squad.squad.filter(dead=False):
            if player.user == request.user:
                player_now = player
                break

    return render(request, 'women/show_map_new.html', {
        'player': player_now,
        'maps': map,
        'room_name': f'{game_slug}/{maps_slug}',
        'messageHistory': messageHistory,
        'menu': menu,
    })

# def attack(request, player_id):
#     if request.is_ajax() and player_id != 0:
#         attr_tt = Player.objects.get(pk=player_id).attr_tt


