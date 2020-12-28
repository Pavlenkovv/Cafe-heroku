from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Category, Dish


def get_main_page(request):
    category = Category.objects.all().order_by('category_order')
    dish = Dish.objects.all()

    context = {'title': 'Густо кафе',
               'about_title': 'Наша історія',
               'categories': category,
               'dishes': dish}
    return render(request, 'index.html', context=context)
