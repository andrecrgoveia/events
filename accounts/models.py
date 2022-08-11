#  Django's imports
from django.db import models

# Developer's imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Managers' imports
from .managers import CustomUserManager


# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Here we can select parameters for login and forms
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # All objects will be manager by UserManager class
    objects = CustomUserManager()

    def __str__(self):
        return self.email
