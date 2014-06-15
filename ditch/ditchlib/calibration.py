
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
                print("Setting calibration from DB")
                cal = e[0]
                self.d_offset = cal.ditch_slope
                self.d_scale = cal.ditch_scale

                self.s_offset = cal.sump_slope
                self.s_scale = cal.sump_scale

        except:
            print("Failed to update calibration.")




    def ditch_inches(self,ditch_val):
        """
         Calculate inches from info data.
        :param info:
        :return:
        """

        try:
            val = float(ditch_val)
        except:
            val = 0.0

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


