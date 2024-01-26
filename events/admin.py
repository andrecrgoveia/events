from django.contrib import admin

from .models import Event, Subscription


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Registering Events models."""
    
    # Displaying data in admin panel
    list_display = ('title', 'user', 'description', 'date', 'created', 'modified', 'active',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Registering Subscription models."""
    
    # Displaying data in admin panel
    list_display = ('subscribed_event', 'subscribed_user',)
