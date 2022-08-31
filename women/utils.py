from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        # {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Добавить игру", 'url_name': 'add_game'},
        {'title': "Добавить команду", 'url_name': 'add_squad'},
        {'title': "Войти в игру", 'url_name': 'join_game'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            for i in range(3):
                user_menu.pop(1)

        context['menu'] = user_menu

        # context['cats'] = cats
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context
