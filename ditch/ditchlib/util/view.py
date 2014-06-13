import os.path
import re

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.shortcuts import redirect
from django.contrib.auth import logout

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class DitchMixin(object):
    angular_app = 'gardenbuzz'

    def get_context_data(self, **kwargs):
        context = super(DitchMixin,self).get_context_data(**kwargs)

        context.update({
            "angularapp": self.angular_app
            })
        return context

class LoginReqMixin(object):
    u""" Insure user is logged in before accessing the view """

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginReqMixin, self).dispatch(request, *args, **kwargs)


def get_redirect(r):
    '''This function is used by the SignUp and Login views.'''
    redirect_url = None
    if r.GET.get('next'):
        redirect_url = r.GET.get('next')
        if r.GET.get('fiddle'):
            redirect_url = redirect_url + '&fiddle=1'
    return redirect_url

def logout_user(r):
    logout(r)
    return redirect("home")


