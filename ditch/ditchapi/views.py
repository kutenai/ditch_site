from django.shortcuts import render

import json

from ditchlib.generic.view import BASEAPIListView,CSRF_Exempt_View
from ditchlib.util.view import LoginReqMixin

from ditchtasks.tasks import status,north_enable,south_enable,pump_enable

class StatusView(BASEAPIListView):

    def get(self,request):

        print("Query Status..")
        r = status.delay()

        try:
            stat = r.get(timeout=10)
            ditch_status = json.loads(stat)
        except:
            ditch_status = {
                'status' : 'Timeout'
            }

        response = self.process_response(ditch_status)
        return response

class ZoneControl(CSRF_Exempt_View):

    def post(self,request,zone='north',onoff='on'):

        bOn = onoff == 'on'

        if zone == 'north':
            print("Calling task:%s" % north_enable.name)
            north_enable.delay(bOn)
        else:
            print("Calling task:%s" % south_enable.name)
            south_enable.delay(bOn)

        return self.process_response({})

class PumpControl(CSRF_Exempt_View):

    def post(self,request,onoff='on'):

        bOn = onoff == 'on'

        pump_enable.delay(bOn)

        return self.process_response({})


