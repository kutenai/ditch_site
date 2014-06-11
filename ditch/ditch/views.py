# Create your views here.
from __future__ import absolute_import

from django.views.generic import TemplateView,FormView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)

        info = {
            'ditch_inches' : 12.2,
            'sump_inches'  : 14.3,
            'pump_on'       : False,
            'north_on'      : False,
            'south_on'      : False
        }
        context['info'] = info
        return context

class AboutView(TemplateView):
    template_name = 'about.html'



