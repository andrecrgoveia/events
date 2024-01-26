from django import forms

from events.models import Event, Subscription


class EventCreationForm(forms.ModelForm):
    """Form to create events."""

    class Meta:
        model = Event
        fields = ('title', 'description', 'date',)
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text'}),
            'description': forms.Textarea(attrs={'type': 'text'}),
            'date': forms.TextInput(attrs={'type': 'date'})
        }


class EventUpdateForm(forms.ModelForm):
    """Form to update events."""

    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'active')
        widgets = {
                'title': forms.TextInput(attrs={'type': 'text'}),
                'description': forms.Textarea(attrs={'type': 'text'}),
                'date': forms.TextInput(attrs={'type': 'date'}),
                'active': forms.CheckboxInput()
            }


class EventSubscriptionForm(forms.ModelForm):
    """Form to subscribe in events."""

    class Meta:
        model = Subscription
        fields = ()  # There is no need to declare the fields here, as they are being dynamically configured in the view

    def form_valid(self, form):
        event_id = self.kwargs['pk']
        form.instance.subscribed_user = self.request.user
        form.instance.subscribed_event_id = event_id
        return super().form_valid(form)
