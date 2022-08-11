# Developer's imports
from django import forms

# Models Events' imports
from events.models import Event


# Form to create events
class EventCreationForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('user', 'title', 'description', 'date',)
        widgets = {
            'user': forms.TextInput(attrs={'type': 'text'}),
            'title': forms.TextInput(attrs={'type': 'text'}),
            'description': forms.TextInput(attrs={'type': 'text'}),
            'date': forms.TextInput(attrs={'type': 'date'})
        }
