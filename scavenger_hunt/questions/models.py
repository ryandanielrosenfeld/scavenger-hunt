from django.db import models


class Task(models.Model):
    number = models.IntegerField()
    activate = models.BooleanField(default=False)
