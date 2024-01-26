from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from events.models import Event, Subscription


class EventsTests(TestCase):
    """Events' test."""

    def create_event(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='normal_password')
        return Event.objects.create(user=user, title='title', description='description', date=timezone.now())

    def test_create_event(self):
        event = self.create_event()
        self.assertTrue(isinstance(event, Event))


class SubscriptionsTests(TestCase):
    """Subscriptions' test."""

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
