import melodist
import pandas as pd


def setup_station():
    df_hourly = pd.read_csv('tests/data/debilt.csv.gz', index_col=0, parse_dates=True)
    df_hourly.temp += 273.15

    df_daily = melodist.util.daily_from_hourly(df_hourly)

    station = melodist.Station(lon=5.18, lat=52.10, timezone=1, data_daily=df_daily)
    station.statistics = melodist.StationStatistics(data=df_hourly)

    return station