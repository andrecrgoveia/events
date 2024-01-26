from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser


class SignUpView(generic.CreateView):
    """This class makes a form to subscribed new users."""

    form_class = CustomUserCreationForm  # This form is used to create new users
    template_name = 'registration/signup.html'

    # This function redirect to login url when the new user is created
    def get_success_url(self):
        return reverse('login')


@method_decorator(login_required, name='dispatch')
class EmailUpdateView(UpdateView):
    """This class makes a form to update users."""

    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/emailupdate.html'
    # fields = ['email',]

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj != self.request.user:
            raise PermissionDenied("You do not have permission to edit this user.")
        return obj

    # This function redirect to login url when the user was updated
    def get_success_url(self):
        return reverse('login')
