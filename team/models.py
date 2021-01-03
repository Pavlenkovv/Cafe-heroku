from django.db import models
from os import path
from uuid import uuid4


class Team(models.Model):
    def get_file_name_team(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/team/', filename)

    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    photo = models.ImageField(upload_to=get_file_name_team, null=True)

    def __str__(self):
        return self.title