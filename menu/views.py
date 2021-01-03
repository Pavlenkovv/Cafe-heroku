from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish

def dish_detail(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    return HttpResponse(f'<h1>Назва: {dish.title}</h1><h1>Ціна: {dish.price}</h1><h1>Опис: {dish.description}</h1>')

def list_categories(request, dish_detail):
    context = {}
    return render(request, 'index.html', context=context)