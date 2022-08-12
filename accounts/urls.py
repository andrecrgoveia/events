# Developer's imports
from django.urls import path

# View's imports
from .views import *


urlpatterns = [
    # View to subscribe new users
    path('signup/', SignUpView.as_view(), name='signup'),
    # View to update users
    path('emailupdateview/<int:pk>/', EmailUpdateView.as_view(), name='emailupdateview'),
]