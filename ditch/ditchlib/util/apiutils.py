import re

from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, allowed_host='*', **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def stripslashes(string):
    """Strips any beginning or trailing slash
    """
    return re.sub("^/|/$", "", string)


def get_http_protocol(request):
    """Returns the protocol used of the request object"""
    if request.is_secure():
        return 'https'
    return 'http'
