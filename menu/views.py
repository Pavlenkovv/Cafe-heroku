from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish


def categories(request, dish_detail):
    items = ['Холодні страви', 'Гарячі страви', 'Напої', 'Ковбаси']
    res = ''
    for item in items:
        res += f'<div><h2>{item}</h2></div>'
    return HttpResponse(res)
