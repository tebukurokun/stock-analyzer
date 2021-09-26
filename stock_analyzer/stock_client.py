from typing import List

import pandas_datareader.data as web
import datetime as datetime
from pandas import DataFrame


def get_my_stock(stock_list: List[str], data_source: str, start: datetime.datetime, end: datetime.datetime,
                 col: str) -> DataFrame:
    df = web.DataReader(stock_list, data_source, start=start, end=end)[col]
    df.to_csv("raw-data.csv")

    return DataFrame(df)


if __name__ == '__main__':
    # 欲しい銘柄のティッカーを指定

    # stock_list = ["AAPL", "AMZN", "FB", "MSFT", "GOOGL", "^DJI"]
    stocks = ["^N225"]

    sample_data_source = 'yahoo'

    # 取得期間を指定
    startTime = datetime.datetime(2021, 9, 1)
    endTime = datetime.datetime(2021, 9, 30)

    get_my_stock(stocks, sample_data_source, startTime, endTime, col="Adj Close")
