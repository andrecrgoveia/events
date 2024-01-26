from django.urls import path

from .views import SignUpView, EmailUpdateView


urlpatterns = [
    # View to subscribe new users
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # View to update users
    path('emailupdate/<int:pk>/', EmailUpdateView.as_view(), name='emailupdate'),
]