from django.shortcuts import render
from django.http import HttpResponse


def get_main_page(request):
    context = {'title': 'Густо кафе',
               'about_title': 'Наша історія'}
    return render(request, 'index.html', context=context)
