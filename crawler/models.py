from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    reciever = models.URLField(null=True)

    def __str__(self):
        return str(self.username)
