#!/usr/bin/python4
import line_profiler
import datetime

@profile
def slow_date_midpoint(date_A, date_B, fmt):
    """
    """
    return datetime.datetime.strptime(date_A, fmt) \
            + (datetime.datetime.strptime(date_A, fmt) - datetime.datetime.strptime(date_B, fmt)) / 2

@profile
def fast_date_midpoint(date_A, date_B):
    """
    """
    return date_A + (date_A - date_B) / 2

# do it with strings and strptime
slow_date_midpoint('1987-01-11', '2001-06-13', '%Y-%m-%d')

# do it with datetimes
fast_date_midpoint(datetime.datetime(year=1987, month=1, day=11),
                   datetime.datetime(year=2001, month=6, day=13))

