from django.db import models


class Task(models.Model):
    number = models.IntegerField()
    activated = models.BooleanField(default=False)
