from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Category, Dish


def get_main_page(request):
    category = Category.objects.filter(is_visible=True).order_by('category_order')

    for item in category:
        item.dishes = Dish.objects.filter(category=item.id)

    special_menu = Dish.objects.filter(category__title='Акції')

    context = {'title': 'Густо кафе',
               'about_title': 'Наша історія',
               'categories': category,
               'special_menu': special_menu
               }
    return render(request, 'index.html', context=context)
