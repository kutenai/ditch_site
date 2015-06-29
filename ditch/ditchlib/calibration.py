
from django.conf import settings
from ditchdb.models import DitchCal


class DitchCalibration(object):

    def __init__(self):

        # Bogus default values.
        self.d_offset = 2.2
        self.d_scale = 0.2

        self.s_offset = 3.2
        self.s_scale = 0.4

        self.updateValues()

    def updateValues(self):

        try:
            e = DitchCal.objects.all()
            if e.count() > 0:
                cal = e[0]
                self.d_offset = cal.ditch_slope
                self.d_scale = cal.ditch_scale
                self.empty_lvl = cal.ditch_empty
                self.alarm_lvl = cal.ditch_alarm

                self.s_offset = cal.sump_slope
                self.s_scale = cal.sump_scale

        except:
            print("Failed to update calibration.")

    def _clean_val(self, in_value, default=0.0):
        """Cast to float, with default if failed."""

        try:
            val = float(in_value)
        except:
            val = default

        return val


    def check_alarm(self, ditch_val):
        """
        Return true if we are in an alarm state.
        :param ditch_val:
        :return:
        """
        val = self._clean_val(ditch_val, 750)
        return val <= self.alarm_lvl

    def check_empty(self, ditch_val):
        """Return true if the ditch is just < than our sensor. """
        val = self._clean_val(ditch_val, 750)
        return val >= self.empty_lvl

    def ditch_inches(self,ditch_val):
        """
         Calculate inches from info data.
        :param info:
        :return:
        """

        val = self._clean_val(ditch_val, 750)
        return (val * self.d_scale) + self.d_offset

    def sump_inches(self,sump_val):
        """
        Calculate sump inches from value
        :param sump_val:
        :return:
        """
        try:
            val = float(sump_val)
        except:
            val = 0.0

        return (val * self.s_scale) + self.s_offset


