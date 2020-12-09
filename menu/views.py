from django.shortcuts import render
from django.http import HttpResponse


def categories(request):
    print(request)
    print(dir(request))

    items = ['Холодні страви', 'Гарячі страви', 'Напої', 'Ковбаси']
    res = ''
    for item in items:
        res += f'<div><h2>{item}</h2></div>'
    return HttpResponse(res)
