# Djangos' imports
from django.test import TestCase

# Developer's imports
from django.utils import timezone
from django.contrib.auth import get_user_model


# Forms' imports
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='normal_password')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username does not exist for this web application
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="normal_password")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='super_password')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username does not exist for this web application
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='super_password', is_superuser=False)


# form's test
class CustomUserFormTests(TestCase):

    def test_user_creation_form(self):
        self.email = 'new@user.com'
        self.is_staff = True
        self.is_active = True
        self.date_joined = timezone.now()

        self.data = {
            'email': self.email,
            'is_staff': self.is_staff,
            'is_active': self.is_active,
            'date_joined': self.date_joined
        }

        self.form = CustomUserCreationForm(data=self.data)

    def test_user_change_form(self):
        self.email = 'another@user.com'
        self.is_staff = True
        self.is_active = True
        self.date_joined = timezone.now()

        self.data = {
            'email': self.email,
            'is_staff': self.is_staff,
            'is_active': self.is_active,
            'date_joined': self.date_joined
        }

        self.form = CustomUserChangeForm(data=self.data)
