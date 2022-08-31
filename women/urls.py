from django.urls import path, re_path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('admin/', admin.site.urls, name='myadmin'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('addgame/', add_game_view, name='add_game'),
    path('addsquad/', AddSquad.as_view(), name='add_squad'),
    path('addplayer/', item_desc_view, name='add_player'),
    path(r'^/(?P<pk>\d+)/addmap/$', create_map, name='add_map'),
    path(r'^updatemap/(?P<pk>\w+)/$', map_update, name='update_map'),
    path('<int:pk>/deletemap/', map_delete, name='delete_map'),
    path('joingame/', join_game_view, name='join_game'),
    path('game/<slug:game_slug>/', ShowGame.as_view(), name='game'),
    path('maps/<slug:game_slug>/<slug:maps_slug>/', mapShow, name='maps'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', update_profile, name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]
