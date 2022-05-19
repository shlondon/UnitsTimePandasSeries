# coding: utf-8
import pandas as pd
import random


# Build a daily pandas series where index is a daily datetime.timestamp object
def daily_pandas_series(start, end):
    """
    Create Docstring
    """
    days = pd.date_range(start,end,freq='D')
    pandas_series = pd.Series([random.uniform(1,10) for i in range(len(days))])
    pandas_series.index = days
    return pandas_series

# Test daily_pandas_series(start, end)