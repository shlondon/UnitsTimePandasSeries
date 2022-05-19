# coding: utf-8

# Class
class unitsTime:

    # Init
    def __init__(self):
        return None

    # Create time series metric with week as units of time
    def weekly(self, daily_time_series):
        """Create DocString
        input: daily_time_series is a pandas.series object where
            index is a daily datetime.timestamp object
        output: a pandas.series object where 
            index is a weekly datetime.timestamp object
        """
        # Weekly
        # Identify index from begins the selection
        for select_from, day in enumerate(daily_time_series.index):
            if day.day_name() == 'Monday':
                break
        
        # Identify index from ends the selection
        for select_to, day in enumerate(reversed(daily_time_series.index)):
            if day.day_name() == 'Sunday':
                break

        # Select complete weeks
        daily_time_series_weekly = daily_time_series[select_from:len(daily_time_series) - select_to]
        
        # Verify if there is one weeks at least
        if len(daily_time_series_weekly) >= 7:
            daily_time_series_weekly = daily_time_series_weekly.resample('W-SUN').sum()
            return daily_time_series_weekly
        else:
            print('There isn´t enough data to create time series weekly')
            return None

    def monthly(self, daily_time_series):
        """Create DocString
        input: daily_time_series is a pandas.series object where
            index is a daily datetime.timestamp object
        output: a pandas.series object where 
            index is a monthly datetime.timestamp object
        """
        # Identify index from begins the selection
        for select_from, day in enumerate(daily_time_series.index):
            if day.is_month_start:
                break

        # Identify index from ends the selection
        for select_to, day in enumerate(reversed(daily_time_series.index)):
            if day.is_month_end:
                break

        # Select complete month  
        daily_time_series_monthly = daily_time_series[select_from:len(daily_time_series) - select_to]
        
        # Verify if there is one month at least
        if len(daily_time_series_monthly) >= 28:
            daily_time_series_monthly = daily_time_series_monthly.resample('M').sum()
            return daily_time_series_monthly
        else:
            print('There isn´t enough data to create time series monthly')
            return None

    # Create time series metric with year as units of time
    def yearly(self, daily_time_series):
        """Create DocString
        input: daily_time_series is a pandas.series object where
            index is a daily datetime.timestamp object
        output: a pandas.series object where 
            index is a yearly datetime.timestamp object
        """
        # Identify index from begins the selection
        for select_from, day in enumerate(daily_time_series.index):
            if day.is_year_start:
                break

        # Identify index from ends the selection
        for select_to, day in enumerate(reversed(daily_time_series.index)):
            if day.is_year_end:
                break

        # Select complete year
        daily_time_series_yearly = daily_time_series[select_from:len(daily_time_series) - select_to]
        
        # Verify if there is one year at least
        if len(daily_time_series_yearly) >= 365:
            daily_time_series_yearly = daily_time_series_yearly.resample('Y').sum()
            return daily_time_series_yearly
        else:
            print('There isn´t enough data to create time series yearly')
            return None

