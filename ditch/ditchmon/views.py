# Create your views here.
from datetime import timedelta, tzinfo, datetime
from django.shortcuts import render_to_response

from ditchdb.models import DitchLog

def index(request,hours=2):
    start = datetime.now() - timedelta(hours=hours)
    entries = DitchLog.objects.filter(timestamp__gte=start)

    return render_to_response('ditchmon.html', {'entries' : entries})

def query(request,hours):

    start = datetime.now() - timedelta(hours=hours)
    entries = DitchLog.objects.filter(timestamp_gte=start)

    return render_to_response('ditchmon.html', {'entries' : entries})


def levels(request):
    start = datetime.now() - timedelta(days=21)
    entries = DitchLog.objects.filter(timestamp__minute=0)

    #conn = DBConnection()
    #dbTable = DBDitch(conn)

    #readings = dbTable.queryLastNReadings(1000)

    #print("Done. Retrieved %d records" % len(readings))

    x = [r.timestamp.strftime("%Y %m %d %H:%M") for r in entries]
    y = [r.ditch_inches for r in entries]

    return render_to_response('ditchlevels.html', {'readings' : {'x' : x, 'y': y}})
