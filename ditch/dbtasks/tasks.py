from __future__ import absolute_import

import json
import redis

from celery import shared_task,chain
from ditchtasks.tasks import status

from celery.utils.log import get_task_logger

logger = get_task_logger('ditch')

@shared_task()
def update_database():

    r = redis.StrictRedis(host='gardenbuzz.com', port=6379, db=3)
    try:
        stat = r.get('ditch_status')
        onstatus.delay(stat)
        print("Updated database with latest status.")
    except:
        print("exception updating database.")

    #ch = chain(status.s() | onstatus.s())
    #ch.apply_async()


@shared_task()
def onstatus(st):
    """
    Handle the status results
    """
    print("Logging results to the database...")

    st = json.loads(st)

    from ditchdb.models import DitchLog

    ll = DitchLog.objects.create(
        ditchlvl    = st.get('Ditch'),
        sumplvl     = st.get('Sump'),
        pump_call   = st.get('PC') == '1',
        pump_on     = st.get('P') == '1',
        north_call  = st.get('NC') == '1',
        north_on    = st.get('N') == '1',
        south_call  = st.get('SC') == '1',
        south_on    = st.get('S') == '1',
    )

    ll.save()

    logger.info("Inserted new status entry.")

    return {"Status" : "Success"}

