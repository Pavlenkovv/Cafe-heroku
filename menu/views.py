from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish
from booking.models import Booking

def dish_detail(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    # return HttpResponse(f'<h1>Назва: {dish.title}</h1><h1>Ціна: {dish.price}</h1><h1>Опис: {dish.description}</h1>')
    reserve_info = Booking.objects.get(pk=1)
    special_menu = Dish.objects.filter(category__title='Акції')
    context = {'title': 'Густо кафе',
                'dish': dish,
               'reserve_info': reserve_info,
               'special_menu': special_menu
               }

    return render(request, 'dish.html', context=context)




def list_categories(request, dish_detail):
    context = {}
    return render(request, 'index.html', context=context)