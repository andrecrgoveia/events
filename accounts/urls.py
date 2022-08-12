# Developer's imports
from django.urls import path

# View's imports
from .views import *


urlpatterns = [
    # View to subscribe new users
    path('signup/', SignUpView.as_view(), name='signup'),
    # View to update users
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='userupdate'),
]