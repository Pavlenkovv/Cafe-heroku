from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import GroupRequiredMixin

from booking.models import Booking
from .forms import *


def is_member(user):
    return user.groups.filter(name='manager').exists() or user.is_staff


def dish_detail(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    reserve_info = Booking.objects.get(pk=1)
    special_menu = Dish.objects.filter(category__title='Акції')
    context = {'title': 'Gusto cafe',
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


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Add Success</h1>')
    else:
        form = DishForm()
    return render(request, 'add_dish.html', context={'form': form})


@login_required(login_url='/login/')
@user_passes_test(is_member)
def categories_view(request):
    items = Category.objects.all().order_by('category_order')
    return render(request, 'categories_view.html', context={'items': items})


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('menu:categories_view')
    success_message = 'Категорія успішно відкоригована!'


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('menu:categories_view')
    success_message = 'Категорія успішно створена!'


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    success_url = reverse_lazy('menu:categories_view')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категорія успішно видалена!')
        return self.post(request, *args, **kwargs)


@login_required(login_url='/login/')
@user_passes_test(is_member)
def dishes(request):
    items = Dish.objects.all()
    return render(request, 'dishes_view.html', context={'items': items})


class DishUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_update.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно відкоригована!'


class DishAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_add.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно створена!'


class DishDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    success_url = reverse_lazy('menu:dishes')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Страва успішно видалена!')
        return self.post(request, *args, **kwargs)
