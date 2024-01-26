from django.urls import path

from .views import (
    AllEventsListView,
    UserEventsListView,
    EventsCreateView,
    EventsUpdateView,
    EventsDeleteView,
    EventSubscriptionView,
    EventUnsubscriptionView,
)


urlpatterns = [
    # Path to show all events
    path('alleventslist/', AllEventsListView.as_view(), name='alleventslist'),

    # Path to show all user's events
    path('usereventslist/', UserEventsListView.as_view(), name='usereventslist'),

    # Path to create events
    path('eventscreate/', EventsCreateView.as_view(), name='eventscreate'),

    # Path to edit events
    path('eventsupdate/<int:pk>/', EventsUpdateView.as_view(), name='eventsupdate'),

    # Path to delete events
    path('eventsdelete/<int:pk>/', EventsDeleteView.as_view(), name='eventsdelete'),

    # Path to sign up an event
    path('eventsubscription/<int:pk>/', EventSubscriptionView.as_view(), name='eventsubscription'),

    # Path to sign up an event
    path('eventunsubscription/<int:pk>/', EventUnsubscriptionView.as_view(), name='eventunsubscription'),
]
