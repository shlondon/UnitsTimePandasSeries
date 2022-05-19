# coding: utf-8
import pandas as pd
import random
from unitsTimeDailyPandasSeries import unitsTime

# Build a daily pandas series where index is a daily datetime.timestamp object
def daily_pandas_series(start, end):
    """
    Create Docstring
    input: start and end days ["2022-02-05"]
    output: pandas.series with index like daily datetime.timestamp and 
        values generated with random.uniform() method
    """
    days = pd.date_range(start,end,freq='D')
    pandas_series = pd.Series([random.uniform(1,10) for i in range(len(days))])
    pandas_series.index = days
    return pandas_series

# Test monthly method
# daily pandas series
daily_ps = daily_pandas_series('2021-01-01', '2025-06-06')
print(daily_ps)

# Start unitsTime instance
ut = unitsTime()

# Yearly pandas series
yearly_ps = ut.yearly(daily_ps)
print(yearly_ps)

# # Test monthly method
# # daily pandas series
# daily_ps = daily_pandas_series('2021-01-02', '2021-06-06')
# print(daily_ps)

# # Start unitsTime instance
# ut = unitsTime()

# # Monthly pandas series
# monthly_ps = ut.monthly(daily_ps)
# print(monthly_ps)

# # Test monthly method
# # daily pandas series
# daily_ps = daily_pandas_series('2021-05-24', '2021-06-06')
# print(daily_ps)

# # Start unitsTime instance
# ut = unitsTime()

# # Weekly pandas series
# weekly_ps = ut.weekly(daily_ps)
# print(weekly_ps)

# # Test daily_pandas_series(start, end)
# print(daily_pandas_series('2021-01-01', '2022-01-01'))