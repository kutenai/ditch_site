from django.shortcuts import render

import json
import redis
from datetime import datetime, timedelta

from ditchlib.generic.view import BASEAPIListView,CSRF_Exempt_View
from ditchlib.util.view import LoginReqMixin
from ditchlib.calibration import DitchCalibration
from ditchlib.mixins import NeverCacheMixin
from ditchlib.Ditch.Controller import DitchController
from ditchdb.models import DitchLog

from ditchtasks.tasks import status,north_enable,south_enable,pump_enable

class StatusView(NeverCacheMixin,BASEAPIListView):

    def __init__(self,*args,**kwargs):
        self.cal = DitchCalibration()
        super(StatusView,self).__init__(*args,**kwargs)

    def get(self,request):

        r = redis.StrictRedis(host='gardenbuzz.com', port=6379, db=5)

        try:
            stat = r.get('ditch_status')

            full_status = json.loads(stat)

            dlvl = full_status.get('Ditch','0.0')
            slvl = full_status.get('Sump','0.0')

            ditch_status = {
                'ditch_reading': dlvl,
                'sump_reading' : slvl,
                'ditch_inches' : self.cal.ditch_inches(dlvl),
                'ditch_empty'  : self.cal.check_empty(dlvl),
                'ditch_alarm'  : self.cal.check_alarm(dlvl),
                'sump_inches'  : self.cal.sump_inches(slvl),
                'pump_on'      : full_status.get('P','0') == '1',
                'north_on'     : full_status.get('N','0') == '1',
                'south_on'     : full_status.get('S','0') == '1',
                'pump_call'    : full_status.get('PC','0') == '1',
                'north_call'   : full_status.get('NC','0') == '1',
                'south_call'   : full_status.get('SC','0') == '1'
            }

            if self.cal.check_alarm(dlvl):
                # Send a notification
                pass


        except Exception as e:

            print("Exception reading status:%s" % e)
            ditch_status = {
                'ditch_inches' : 0.0,
                'sump_inches'  : 0.0,
                'pump_on'      : False,
                'north_on'     : False,
                'south_on'     : False,
                'pump_call'    : False,
                'north_call'   : False,
                'south_call'   : False,
            }

        response = self.process_response(ditch_status)
        return response

class ZoneControl(DitchController, CSRF_Exempt_View):


    def post(self,request,zone='north',onoff='on'):

        bOn = onoff == 'on'

        if zone == 'north':
            print("Calling task:%s" % north_enable.name)
            self.northEnable(bOn)
        else:
            print("Calling task:%s" % south_enable.name)
            self.southEnable(bOn)

        return self.process_response({})

class PumpControl(DitchController, CSRF_Exempt_View):

    def post(self,request,onoff='on'):

        bOn = onoff == 'on'
        self.pumpEnable(bOn)

        return self.process_response({})

class HistoryView(CSRF_Exempt_View):
    """
    Return the history of the ditch levels.
    """

    def get(self, request):

        start_at = request.GET.get('start_at', None)

        if start_at:
            log = DitchLog.objects.filter(timestamp__gt=start_at).values_list('timestamp', 'ditch_inches', 'sump_inches')
        else:
            days_30 = datetime.now().date() + timedelta(days=-30)
            log = DitchLog.objects.filter(timestamp__gte=days_30).values_list('timestamp', 'ditch_inches', 'sump_inches')

            if log.count() == 0:
                log = DitchLog.objects.all().values_list('timestamp', 'ditch_inches', 'sump_inches')

        results = {'data': log}
        if len(log):
            results['newest'] = log[len(log)-1][0]

        return self.process_response(results)




