from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class DitchCal(models.Model):
    """
    Calibration factors to use for converting sump and ditch
    measured values to actual values.
    """

    ditch_slope     = models.FloatField(default=-0.0106)
    ditch_scale     = models.FloatField(default=14.0)
    ditch_empty     = models.FloatField(default=720)
    ditch_alarm     = models.FloatField(default=50)

    sump_slope      = models.FloatField(default=-3.034)
    sump_scale      = models.FloatField(default=0.037)

@python_2_unicode_compatible
class DitchLog(models.Model):
    timestamp       = models.DateTimeField(auto_now=True)
    ditchlvl        = models.IntegerField(default=0)
    sumplvl         = models.IntegerField(default=0)
    ditch_inches    = models.FloatField(default=0.0)
    sump_inches    = models.FloatField(default=0.0)
    pump_call       = models.BooleanField(default=0)
    pump_on         = models.BooleanField(default=0)

    north_call      = models.BooleanField(default=0)
    north_on        = models.BooleanField(default=0)

    south_call      = models.BooleanField(default=0)
    south_on        = models.BooleanField(default=0)

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






