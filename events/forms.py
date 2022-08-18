# Developer's imports
from django import forms

# Models Events' imports
from events.models import Event, Subscription


# Form to create events
class EventCreationForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('user', 'title', 'description', 'date',)
        widgets = {
            'user': forms.TextInput(attrs={'type': 'text'}),
            'title': forms.TextInput(attrs={'type': 'text'}),
            'description': forms.Textarea(attrs={'type': 'text'}),
            'date': forms.TextInput(attrs={'type': 'date'})
        }


# Form to update events
class EventUpdateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('user', 'title', 'description', 'date', 'active')
        widgets = {
                'user': forms.TextInput(attrs={'type': 'text'}),
                'title': forms.TextInput(attrs={'type': 'text'}),
                'description': forms.Textarea(attrs={'type': 'text'}),
                'date': forms.TextInput(attrs={'type': 'date'}),
                'active': forms.CheckboxInput()
            }


# Form to subscribe in an event
class EventSubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ('subscribed_user', 'subscribed_event',)
