from django.urls import path, include
from .views import dish_detail, list_categories


urlpatterns = [
     # path('', categories)
     path('<int:dish_id>/', dish_detail, name='dish_detail'),
]