from django.conf.urls import patterns, include, url

from django.conf import settings
from ditch.admin import site
from django.contrib import admin
admin.autodiscover()

from views import AboutView,HomeView
from profiles.views import (
    LoginView,
    LoggedInView,
    PasswordResetView,
    ChangePasswordView
)
from ditchlib.util.view import logout_user

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^mon/', include ('ditchmon.urls'),name='mon'),
    url(r'^ctrl/', include ('ditchctrl.urls'),name='ctrl'),
    url(r'^about/', AboutView.as_view(),name='about'),
    url(r'^contact/', AboutView.as_view(),name='contact'),
    url(r"^admin/", include(site.urls)),
    url(r"^api/%s/" % settings.API_VERSION, include('ditchapi.urls',namespace='api')),
)

urlpatterns += patterns('',
    url(r"^account/login/$", LoginView.as_view(), name="account_login"),
    url(r"^account/logout/?$", logout_user, name="account_logout"),
    url(r"^account/logged-in/$", LoggedInView.as_view(), name="account_loggedin"),
    url(r"^account/password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    url(r"^account/password/?$", ChangePasswordView.as_view(), name="account_password"),
)

