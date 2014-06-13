from django.shortcuts import render

import json

from ditchlib.generic.view import BASEAPIListView
from ditchlib.util.view import LoginReqMixin

from ditchtasks.tasks import status

class StatusView(LoginReqMixin,BASEAPIListView):

    def get(self,request):

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
