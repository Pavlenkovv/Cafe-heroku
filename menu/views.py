from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish
from booking.models import Booking
from .forms import CategoryForm


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


def list_categories(request):
    context = {}
    return render(request, 'index.html', context=context)



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Add Success</h1>')
    else:
        form = CategoryForm()
        return render(request, 'add_category.html', context={'form': form})


# def add_dish(request):
