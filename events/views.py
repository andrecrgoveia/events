#  Django's imports
from django.shortcuts import render

# Developer's imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Models Accounts'  imports
from accounts.models import CustomUser

# Models Events' imports
from events.models import Event

# Forms' imports
from .forms import EventCreationForm


# In this class we can create events
@method_decorator(login_required, name='dispatch')
class EventsCreateView(CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'events/eventscreateview.html'
    success_url = reverse_lazy('eventslistview')


# This class show all events
@method_decorator(login_required, name='dispatch')
class EventsListView(ListView):
    models = Event
    template_name = 'events/eventslistview.html'

    def get(self, request):
        data = Event.objects.all()

        context = {'data': data}

        return render(request, 'events/eventslistview.html', context)
