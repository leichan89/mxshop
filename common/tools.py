# -*- coding: utf-8 -*-
# @Time    : 2020-07-02 15:11
# @Author  : OG·chen
# @File    : tools.py

import datetime, time

class Tools:

    @staticmethod
    def datetime2timestamp(dt, to11=False):
        timetuple = dt.timetuple()
        second = time.mktime(timetuple)
        if to11:
            return int(second)
        microsecond = int(second * 1000 + dt.microsecond / 1000)
        return microsecond


if __name__ == "__main__":
    t = Tools()
    tt = datetime.datetime.now()
    print(t.datetime2timestamp(dt=tt, to11=True))










