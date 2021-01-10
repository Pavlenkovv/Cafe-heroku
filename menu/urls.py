from django.urls import path
from .views import *


urlpatterns = [

     path('add_category/', add_category, name='add_category'),
     path('add_dish/', add_dish, name='add_dish'),
     path('<int:dish_id>/', dish_detail, name='dish_detail'),


     path('categories/', categories_view, name='categories_view'),
     path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='categories_update'),
     path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories_delete'),
     path('categories/add', CategoryAddView.as_view(), name='categories_add'),

     path('dishes/', dishes, name='dishes'),
     path('dishes/update/<int:pk>/', DishUpdateView.as_view(), name='dishes_update'),
     path('dishes/delete/<int:pk>/', DishDeleteView.as_view(), name='dishes_delete'),
     path('dishes/add', DishAddView.as_view(), name='dishes_add'),
]