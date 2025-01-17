from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)  # Ensure passwords are hashed before storing

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




