# Django's imports
from django.contrib import admin

# Developer's import
from .models import Event


"""Registering models for system admin can edit the data"""

# Here we user a register decorator for this model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Displaying data in admin panel
    list_display = ('title', 'user', 'description', 'date', 'created', 'modified', 'active',)
