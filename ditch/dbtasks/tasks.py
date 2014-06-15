from __future__ import absolute_import

import json

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger('ditch')

@shared_task()
def onstatus(st):
    """
    Handle the status results
    """
    print("On Status Called..")

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

