import pandas_datareader.data as web
import datetime as datetime
import matplotlib.pyplot as plt
import pandas as pd


def main():
    # 取得期間を指定
    start = datetime.datetime(2021, 9, 1)
    end = datetime.datetime(2021, 9, 30)

    # 欲しい銘柄のティッカーを指定
    stock_list = ["AAPL", "AMZN", "FB", "MSFT", "GOOGL"]

    df = web.DataReader(stock_list, 'yahoo', start=start, end=end)
    df.to_csv("raw-data.csv")


if __name__ == '__main__':
    main()
