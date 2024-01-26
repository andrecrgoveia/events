from django.db.models import Count, OuterRef, Exists
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from events.models import Event, Subscription

from .forms import EventCreationForm, EventUpdateForm, EventSubscriptionForm



class UserAccessMixin:
    """Mixin for access control."""
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            raise Http404("You are not allowed to perform this action.")
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AllEventsListView(LoginRequiredMixin, ListView):
    """View to show all events."""
    
    model = Event
    template_name = 'events/alleventslist.html'
    context_object_name = 'all_active_events'
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user

        queryset = (
            Event.objects
            .filter(active=True)
            .annotate(
                participant_count=Count('subscribed_event__subscribed_user', distinct=True),
                user_is_subscribed=Exists(
                    Subscription.objects.filter(
                        subscribed_user=user,
                        subscribed_event=OuterRef('id')
                    )
                )
            )
            .values('id', 'title', 'date', 'user__email', 'participant_count', 'user_is_subscribed')
            .order_by('date')
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            all_active_events = paginator.page(page)
        except PageNotAnInteger:
            all_active_events = paginator.page(1)
        except EmptyPage:
            all_active_events = paginator.page(paginator.num_pages)
        context['all_active_events'] = all_active_events
        return context


@method_decorator(login_required, name='dispatch')
class UserEventsListView(LoginRequiredMixin, ListView):
    """View to show user's events."""
    
    model = Event
    template_name = 'events/usereventslist.html'
    context_object_name = 'user_events'
    paginate_by = 2

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            user_events = paginator.page(page)
        except PageNotAnInteger:
            user_events = paginator.page(1)
        except EmptyPage:
            user_events = paginator.page(paginator.num_pages)
        context['user_events'] = user_events
        return context


@method_decorator(login_required, name='dispatch')
class EventsCreateView(LoginRequiredMixin, CreateView):
    """View to create events."""
    
    model = Event
    form_class = EventCreationForm
    template_name = 'events/eventscreate.html'
    success_url = reverse_lazy('usereventslist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EventsUpdateView(LoginRequiredMixin, UserAccessMixin, UserPassesTestMixin, UpdateView):
    """View to edit events."""
    
    model = Event
    template_name = "events/eventsupdate.html"
    form_class = EventUpdateForm
    success_url = reverse_lazy("usereventslist")

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.user


@method_decorator(login_required, name='dispatch')
class EventsDeleteView(LoginRequiredMixin, UserAccessMixin, UserPassesTestMixin, DeleteView):
    """View to delete events."""
    
    model = Event
    template_name = "events/eventsdelete.html"
    success_url = reverse_lazy('usereventslist')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.user


@method_decorator(login_required, name='dispatch')
class EventSubscriptionView(LoginRequiredMixin, CreateView):
    """View to sign up for events."""
    
    model = Subscription
    form_class = EventSubscriptionForm
    template_name = 'events/eventsubscription.html'
    success_url = reverse_lazy('alleventslist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.get(pk=self.kwargs['pk'])
        context['title'] = event.title
        return context

    def form_valid(self, form):
        event_id = self.kwargs['pk']
        form.instance.subscribed_user = self.request.user
        form.instance.subscribed_event_id = event_id
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EventUnsubscriptionView(LoginRequiredMixin, DeleteView):
    """View to unsubscribe from events."""
    
    model = Subscription
    template_name = "events/eventunsubscription.html"
    success_url = reverse_lazy('alleventslist')

    def get(self, request, *args, **kwargs):
        subscription = get_object_or_404(Subscription, subscribed_user=request.user, subscribed_event=kwargs['pk'])
        return render(request, self.template_name, {'subscription': subscription})

    def delete(self, request, *args, **kwargs):
        subscription = get_object_or_404(Subscription, subscribed_user=request.user, subscribed_event=kwargs['pk'])
        subscription.delete()
        return HttpResponseRedirect(self.success_url)


def bad_request(request, exception):
    """
    View to handle bad requests (status 400).
    Renders a custom error template.
    """
    return render(request, 'error.html', status=400)


def permission_denied(request, exception):
    """
    View to handle permission denied (status 403).
    Renders a custom error template.
    """
    return render(request, 'error.html', status=403)


def page_not_found(request, exception):
    """
    View to handle page not found (status 404).
    Renders a custom error template.
    """
    return render(request, 'error.html', status=404)


def server_error(request):
    """
    View to handle server errors (status 500).
    Renders a custom error template.
    """
    return render(request, 'error.html', status=500)
