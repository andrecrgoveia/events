#  Django's imports
from django.shortcuts import render

# Developer's imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Models Events' imports
from events.models import Event

# Forms' imports
from .forms import *


# This class show all events
@method_decorator(login_required, name='dispatch')
class AllEventsListView(ListView):
    models = Event
    template_name = 'events/alleventslistview.html'

    def get(self, request):
        # Filtering all active events
        data = Event.objects.filter(active=True).order_by('date')

        # Creating a list to receive all active events and their data
        all_active_events = []

        # Making a loop in Events queryset, to better handle with the data and append items in all_active_events list
        for item in data.values():
            all_active_events.append(item)

            # Making a loop in Events queryset to check user_id and append the owner info
            for d in data:
                if int(d.user_id) == int(item.get('user_id')):
                    # This block is used to separate the username from the user's full email
                    username = str(d.user)
                    owner = username[:username.index("@")]
                    item['owner'] = owner

        context = {'all_active_events': all_active_events}

        return render(request, 'events/alleventslistview.html', context)


# This class show all user's events
@method_decorator(login_required, name='dispatch')
class UserEventsListView(ListView):
    models = Event
    template_name = 'events/usereventslistview.html'

    def get(self, request):
        # Getting data from logged user
        logged_user = request.user.id
        # Filtering all active events
        data = Event.objects.filter(user=logged_user).order_by('date')

        context = {'data': data}

        return render(request, 'events/usereventslistview.html', context)


# In this class we can create events
@method_decorator(login_required, name='dispatch')
class EventsCreateView(CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'events/eventscreateview.html'
    success_url = reverse_lazy('usereventslistview')


# In this class we can edit events
@method_decorator(login_required, name='dispatch')
class EventsUpdateView(UpdateView):
    model = Event
    template_name = "events/eventsupdateview.html"
    form_class = EventUpdateForm
    success_url = reverse_lazy("usereventslistview")


# In this class we can edit events
@method_decorator(login_required, name='dispatch')
class EventsDeleteView(DeleteView):
    model = Event
    template_name = "events/eventsdeleteview.html"
    success_url = reverse_lazy('usereventslistview')
