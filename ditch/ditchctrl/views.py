from __future__ import absolute_import

import os
import sys

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from ditchtasks.tasks import status,pump_enable, north_enable, south_enable

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def index(request):
    """
    List all code nurseries, or create a new snippet.
    """
    if request.method == 'GET':
        r = status.delay()
        try:
            stat  = r.get(timeout=10)
            return JSONResponse(stat, status=201)
        except:
            return JSONResponse({}, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if data.has_key('zone'):
            zone = data['zone']
            if zone == 'north':
                north_enable.delay(True)
            elif zone == 'south':
                south_enable.delay(True)

        return JSONResponse({}, status=201)

    elif request.method == 'DELETE':
        print("Deleting. or stopping it")
        pump_enable.delay(False)
        north_enable.delay(False)
        south_enable.delay(False)
        return JSONResponse({}, status=201)

@csrf_exempt
def levels(request):
    """
    List all code nurseries, or create a new snippet.
    """
    if request.method == 'GET':
        r = status.delay()
        try:
            stat  = r.get(timeout=10)
            return JSONResponse(stat, status=201)
        except:
            return JSONResponse({}, status=200)

    else:
        return JSONResponse({}, status=201)


