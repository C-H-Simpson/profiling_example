#!/usr/bin/python4
import line_profiler
import datetime
import numpy as np

# set random seed for reproducibility
np.random.seed(1)

# some random years, months, days
n_dates = 10000
years_A = np.random.choice(range(1999, 2010), n_dates)
months_A = np.random.choice(range(1, 12), n_dates)
days_A = np.random.choice(range(1, 28), n_dates)

years_B = np.random.choice(range(1999, 2010), n_dates)
months_B = np.random.choice(range(1, 12), n_dates)
days_B = np.random.choice(range(1, 28), n_dates)


@profile
def slow_dates():
    """
        This routine loops over a two lists of dates, and finds the
        number of days between them.
        It is slow because it makes the dates as string objects first, then converts
        them to datetimes, instead of making datetime objects directly.
    """

    # make dates as strings
    dates_A = [ '{0}-{1:02d}-{2:02d}'.format(y, m, d) for y, m, d in zip(years_A, months_A, days_A) ]
    dates_B = [ '{0}-{1:02d}-{2:02d}'.format(y, m, d) for y, m, d in zip(years_B, months_B, days_B) ]
    total_difference = 0

    for date_A, date_B in zip(dates_A, dates_B):
        difference = datetime.datetime.strptime(date_A, '%Y-%m-%d') - datetime.datetime.strptime(date_B, '%Y-%m-%d')
        total_difference += difference / datetime.timedelta(days=1)

    print ('total', total_difference, 'days')

@profile
def fast_dates():
    """
    """

    # make dates as datetime objects
    dates_A = [  datetime.date(year=y, month=m, day=d) for y, m, d in zip(years_A, months_A, days_A) ]
    dates_B = [  datetime.date(year=y, month=m, day=d) for y, m, d in zip(years_B, months_B, days_B) ]
    total_difference = 0

    for date_A, date_B in zip(dates_A, dates_B):
        difference = date_A - date_B
        total_difference += difference / datetime.timedelta(hours=1)

    print ('total', total_difference, 'days')


slow_dates()
fast_dates()
