from django.urls import path
from .views import *

urlpatterns = [
    path ('', home, name='messages_info'),
    path('update/<int:pk>/', update_messages, name='update')

]