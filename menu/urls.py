from django.urls import path
from .views import dish_detail, add_category, add_dish


urlpatterns = [
     path('add_category/', add_category, name='add_category'),
     path('add_dish/', add_dish, name='add_dish'),
     path('<int:dish_id>/', dish_detail, name='dish_detail'),
]