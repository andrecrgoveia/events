from django.db import models

from accounts.models import CustomUser


class Base(models.Model):
    """Base model with common fields."""

    id = models.BigAutoField(primary_key=True)
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Event(Base):
    """Model to represent an event."""

    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField('Title', max_length=250, blank=False, null=False)
    description = models.CharField('Description', max_length=500, blank=False, null=False)
    date = models.DateField('Date', blank=False, null=False)

     # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Subscription(Base):
    """Model to represent a subscription to an event."""

    subscribed_user = models.ForeignKey(CustomUser, related_name='subscribed_user', on_delete=models.CASCADE, blank=False, null=False)
    subscribed_event = models.ForeignKey(Event, related_name='subscribed_event', on_delete=models.CASCADE, blank=False, null=False)
    unique_together = ['subscribed_user', 'subscribed_event'] # Adding the uniqueness constraint

     # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return str(self.subscribed_event)
