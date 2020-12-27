from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
