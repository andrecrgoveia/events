# Developer's imports
from django.urls import path

# View's imports
from .views import EventsCreateView, EventsListView


urlpatterns = [
    # Path to create events
    path('eventscreateview/', EventsCreateView.as_view(), name='eventscreateview'),
    # Path to show all events
    path('eventslistview/', EventsListView.as_view(), name='eventslistview'),
]
