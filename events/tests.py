# Djangos' imports
from django.test import TestCase

# Developer's import
from django.utils import timezone
from django.contrib.auth import get_user_model

# Models' imports
from events.models import Event, Subscription

# Forms' imports
from events.forms import EventCreationForm, EventUpdateForm, EventSubscriptionForm


# models' test
class EventsTests(TestCase):

    def create_event(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='normal_password')
        return Event.objects.create(user=user, title='title', description='description', date=timezone.now())

    def test_create_event(self):
        event = self.create_event()
        self.assertTrue(isinstance(event, Event))


class SubscriptionsTests(TestCase):

    def create_event(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='normal_password')
        return Event.objects.create(user=user, title='title', description='description', date=timezone.now())

    def create_subscription(self):
        User = get_user_model()
        user = User.objects.create_user(email='new@user.com', password='new')
        event = self.create_event()
        return Subscription.objects.create(subscribed_user=user, subscribed_event=event)

    def test_create_subscription(self):
        subscription = self.create_subscription()
        self.assertTrue(isinstance(subscription, Subscription))


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


class SubscriptionsFormTests(TestCase):

    def test_event_subscription_form(self):
        self.subscribed_user = 1
        self.subscribed_event = 1

        self.data = {
            'subscribed_user': self.subscribed_user,
            'subscribed_event': self.subscribed_event,
        }

        self.form = EventSubscriptionForm(data=self.data)
