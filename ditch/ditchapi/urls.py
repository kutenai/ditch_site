from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.views.decorators.cache import never_cache

from .views import StatusView, ZoneControl, PumpControl, HistoryView

urlpatterns = patterns('',
                       url(r'status/', never_cache(StatusView.as_view()), name="status"),
                       url(r'(?P<zone>(north|south))/(?P<onoff>(on|off))/',
                           never_cache(ZoneControl.as_view()), name='zone'),
                       url(r'pump/(?P<onoff>(on|off))/',
                           never_cache(PumpControl.as_view()), name='pump'),
                       url(r'history/?$',
                           never_cache(HistoryView.as_view()), name='history'),

                       )
