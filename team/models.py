from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.title