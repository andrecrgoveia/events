from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Here we can select parameters for login and forms
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # All objects will be manager by UserManager class
    objects = CustomUserManager()
    