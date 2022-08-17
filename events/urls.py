# Developer's imports
from django.urls import path

# View's imports
from .views import *


urlpatterns = [
    # Path to show all events
    path('alleventslistview/', AllEventsListView.as_view(), name='alleventslistview'),
    # Path to show all user's events
    path('usereventslistview/', UserEventsListView.as_view(), name='usereventslistview'),
    # Path to create events
    path('eventscreateview/', EventsCreateView.as_view(), name='eventscreateview'),
    # Path to edit events
    path('eventsupdateview/<int:pk>/', EventsUpdateView.as_view(), name='eventsupdateview'),
    # Path to delete events
    path('eventsdeleteview/<int:pk>/', EventsDeleteView.as_view(), name='eventsdeleteview'),
    # Path to sign up an event
    path('eventsubscriptionview/<int:pk>/', EventSubscriptionView.as_view(), name='eventsubscriptionview'),
]
