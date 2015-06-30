from django.views.generic import base

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ditchlib.util.apiutils import JSONResponse

class BASEAPIListView(base.View):

    def __init__(self, *args, **kwargs):
        super(BASEAPIListView, self).__init__(*args, **kwargs)

    def process_response(self, data, value=''):
        return JSONResponse(data, value)


class CSRF_Exempt_View(BASEAPIListView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CSRF_Exempt_View,self).dispatch(request,*args,**kwargs)

