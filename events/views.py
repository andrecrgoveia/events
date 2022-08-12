#  Django's imports
from django.shortcuts import render

# Developer's imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Models Accounts'  imports
from accounts.models import CustomUser # Remover depois????

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
        data = Event.objects.filter(active=True)

        # for item in data:
        #     name = str(item.user)
        #     nome = name[:name.index("@")]
        #     print(nome)

        context = {'data': data}

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
        data = Event.objects.filter(user=logged_user)

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
