#  Django's imports
from django.db import models

# Developer's imports
from accounts.models import CustomUser


"""
This class provides these three parameters for the other classes to inherit and in the django admin,
the superuser can manage the created models.
"""

# This class defines three parameters for easy viewing on the admin panel
class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


# In this class we can create the Event object
class Event(Base):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.DO_NOTHING)
    title = models.CharField('Title', max_length=250, blank=False, null=False)
    description = models.CharField('Description', max_length=500, blank=False, null=False)
    date = models.DateField('Date', max_length=500, blank=False, null=False)

     # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


# In this class we can assign an event
class Subscription(Base):
    subscribed_user = models.ForeignKey(CustomUser, related_name='subscribed_user', on_delete=models.DO_NOTHING)
    subscribed_event = models.ForeignKey(Event, related_name='subscribed_event', on_delete=models.DO_NOTHING)

     # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return self.subscribed_event
