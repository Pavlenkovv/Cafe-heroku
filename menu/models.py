from django.db import models
from os import path
from uuid import uuid4


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Dish(models.Model):
    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes/', filename)

    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to=get_file_name_dishes, null=True)
    spicy = models.BooleanField(default=False)

    def __str__(self):
        return self.title
