from django.views.generic import base

from ditchlib.util.apiutils import JSONResponse

class BASEAPIListView(base.View):
    http_method_names = ['get']

    def __init__(self, *args, **kwargs):
        self.response = JSONResponse

    def process_response(self, data, value=''):
        return self.response(data, value)

