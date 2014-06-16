from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class DitchCal(models.Model):
    """
    Calibration factors to use for converting sump and ditch
    measured values to actual values.
    """

    ditch_slope     = models.FloatField()
    ditch_scale     = models.FloatField()

    sump_slope      = models.FloatField()
    sump_scale      = models.FloatField()

@python_2_unicode_compatible
class DitchLog(models.Model):
    timestamp       = models.DateTimeField(auto_now=True)
    ditchlvl        = models.IntegerField()
    sumplvl         = models.IntegerField()
    pump_call       = models.BooleanField()
    pump_on         = models.BooleanField()

    north_call      = models.BooleanField()
    north_on        = models.BooleanField()

    south_call      = models.BooleanField()
    south_on        = models.BooleanField()

    def __str__(self):
        return """
        @%s Ditch:%s Sump:%s
        Pump %s->%s North %s->%s South %s->%s
""" % (self.timestamp,
       self.ditchlvl,
       self.sumplvl,
       self.pump_call,
       self.pump_on,
       self.north_call,
       self.north_on,
       self.south_call,
       self.south_on)






