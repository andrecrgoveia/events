# Djangos' imports
from django.test import TestCase

# Developer's import
from django.utils import timezone
from django.contrib.auth import get_user_model

# Models' imports
from events.models import Event

# Forms' imports
from events.forms import EventCreationForm, EventUpdateForm


# models' test
class EventsTests(TestCase):

    def create_event(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='normal_password')
        return Event.objects.create(user=user, title='title', description='description', date=timezone.now())

    def test_create_event(self):
        event = self.create_event()
        self.assertTrue(isinstance(event, Event))


# form's test
class EventsFormTests(TestCase):

    def test_create_form(self):
        self.user = 'new_user'
        self.title = 'new_title'
        self.description = 'new_description'
        self.date = timezone.now()

        self.data = {
            'user': self.user,
            'title': self.title,
            'description': self.description,
            'date': self.date
        }

        self.form = EventCreationForm(data=self.data)

    def test_update_form(self):
        self.user = 'new_user'
        self.title = 'new_title'
        self.description = 'new_description'
        self.date = timezone.now()
        self.active = True

        self.data = {
            'user': self.user,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'active': self.active
        }

        self.form = EventUpdateForm(data=self.data)
