from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):
    finished = models.BooleanField(default=False)
    task_num = models.IntegerField(default=0)
    activate1 = models.BooleanField(default=False)
    activate2 = models.BooleanField(default=False)
