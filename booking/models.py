from django.db import models


class Booking(models.Model):
    title = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.title
