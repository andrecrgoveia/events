"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    # Path to django admin
    path('admin/', admin.site.urls),

    # Path to be accounts app
    path('accounts/', include('accounts.urls')),

    # Django module authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # Path to events app
    path('events/', include('events.urls')),

    # Path to home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom handle erros
handler400 = 'events.views.bad_request'
handler403 = 'events.views.permission_denied'
handler404 = 'events.views.page_not_found'
handler500 = 'events.views.server_error'
