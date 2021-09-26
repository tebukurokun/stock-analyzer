import datetime

import numpy as np

from stock_analyzer.plot import plot_price_history, plot_volatility
from stock_client import get_my_stock
import matplotlib.pyplot as plt
import pandas as pd


def main():
    # 欲しい銘柄のティッカーを指定

    # stock_list = ["AAPL", "AMZN", "FB", "MSFT", "GOOGL", "^DJI", "^N225"]
    stocks = ["GOOG", "AMZN", "FB", "AAPL"]

    sample_data_source = 'yahoo'

    # 取得期間を指定
    start_time = datetime.datetime(2020, 9, 1)
    end_time = datetime.datetime(2021, 9, 30)

    col = "Adj Close"

    # 株価データ取得
    my_stocks = get_my_stock(stocks, sample_data_source, start_time, end_time, col=col)

    # １日あたりの変化率
    daily_rate_change = my_stocks.pct_change(1)
    # print(daily_rate_change)

    # 相関
    # print(daily_rate_change.corr())
    # 共分散
    # print(daily_rate_change.cov())
    # 標準偏差
    # print(daily_rate_change.std())

    daily_mean_returns = daily_rate_change.mean()
    print("Dailyn mean return:")
    print(daily_mean_returns)

    portfolio_proportion = np.array([0.4, 0.3, 0.2, 0.1])

    # リターンを計算
    daily_mean_portfolio = np.sum(daily_mean_returns * portfolio_proportion)

    print(str(daily_mean_portfolio))

    # plot
    # plot_price_history(my_stocks, col)

    # plot_volatility(my_stocks)


if __name__ == '__main__':
    main()
