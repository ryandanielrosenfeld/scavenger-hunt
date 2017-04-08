from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):
    finished = models.BooleanField(default=False)
