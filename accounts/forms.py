# Developer's imports
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models' imports
from .models import CustomUser


# Form to create new users
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


# A form to update new users
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
