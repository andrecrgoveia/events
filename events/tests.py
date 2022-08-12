# Djangos' imports
from django.test import TestCase

# Developer's import
from datetime import date, datetime
from django.utils import timezone

# Models' imports
from accounts.models import CustomUser
from events.models import Event






# # models test
# class EventTests(TestCase):

#     def create_event(self):
#         user=CustomUser.objects.filter(id=1)
#         print(CustomUser.objects.filter(id=2))
#         return Event.objects.create(user=user, title='title', description='description', date=timezone.now())

#     def test_event_creation(self):
#         w = self.create_event()
#         self.assertTrue(isinstance(w, Event))
#         self.assertEqual(w.__unicode__(), w.title)

# class EventTests(TestCase):

#     def test_create_event(self):
#         Event = Event.objects.all()
#         event = Event.objects.create(
#             user=1,
#             title='some_title',
#             description='some_description',
#             date=datetime.date(2022, 10, 11)
#             )
#         self.assertEqual(user.email, 'normal@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username does not exist for this web application
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email='', password="normal_password")

#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(email='super@user.com', password='super_password')
#         self.assertEqual(admin_user.email, 'super@user.com')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username does not exist for this web application
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 email='super@user.com', password='super_password', is_superuser=False)
