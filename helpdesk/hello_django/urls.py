from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url
from helpdesk.views import login

urlpatterns = [
    path('', include('helpdesk.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', login.login, name='login'),
    path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # url(r'helpdesk/', include('helpdesk.urls')),
    # url(r"^account/", include("account.urls")),
    url(r"^teams/", include("pinax.teams.urls", namespace="pinax_teams")),
]
