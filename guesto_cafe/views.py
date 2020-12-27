from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Category


def get_main_page(request):
    category = Category.objects.all().order_by('category_order')

    context = {'title': 'Густо кафе',
               'about_title': 'Наша історія',
               'categories': category}
    return render(request, 'index.html', context=context)
