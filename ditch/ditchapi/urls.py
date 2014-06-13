from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import StatusView

urlpatterns = patterns('',
                       url(r'status/?', StatusView.as_view(), name="status"),
                       )


