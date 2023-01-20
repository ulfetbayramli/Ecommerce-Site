from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="User_Profile")
    blank=True
    def __str__(self):
        return self.first_name 

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

