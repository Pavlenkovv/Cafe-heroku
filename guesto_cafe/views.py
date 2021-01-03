from django.shortcuts import render
from menu.models import Category, Dish
from team.models import Team
from booking.models import Booking

def get_main_page(request):
    category = Category.objects.filter(is_visible=True).order_by('category_order')

    for item in category:
        item.dishes = Dish.objects.filter(category=item.id)

    special_menu = Dish.objects.filter(category__title='Акції')

    team_text = Team.objects.get(pk=1)

    reserve_info = Booking.objects.get(pk=1)

    context = {'title': 'Густо кафе',
               'about_title': 'Наша історія',
               'categories': category,
               'special_menu': special_menu,
               'team_text': team_text,
               'reserve_info': reserve_info
               }
    return render(request, 'index.html', context=context)
