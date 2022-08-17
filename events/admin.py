# Django's imports
from django.contrib import admin

# Developer's import
from .models import Event, Subscription


"""Registering models for system admin can edit the data"""

# Here we user a register decorator for this model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Displaying data in admin panel
    list_display = ('title', 'user', 'description', 'date', 'created', 'modified', 'active',)


# Here we user a register decorator for this model
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    # Displaying data in admin panel
    list_display = ('subscribed_user', 'subscribed_event',)
