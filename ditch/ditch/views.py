# Create your views here.
from __future__ import absolute_import

from django.views.generic import TemplateView,FormView
from ditchlib.util.view import LoginReqMixin

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)

        context['angularapp'] = 'ditchapp'
        return context

class AboutView(TemplateView):
    template_name = 'about.html'



