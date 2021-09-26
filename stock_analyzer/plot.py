import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
import pandas as pd


def plot_price_history(stock_data: DataFrame, col: str):
    title = col + " Price History"

    plt.figure(figsize=(18, 8))

    for i in stock_data.columns.values:
        plt.plot(stock_data[i], label=i)

    plt.title(title)

    plt.xlabel("date", fontsize=16)

    plt.ylabel(col + " Price", fontsize=16)

    plt.legend(stock_data.columns.values, loc="upper left")

    plt.show()


def plot_volatility(stock_data: DataFrame):
    plt.figure(figsize=(18, 8))

    daily_rate_change = stock_data.pct_change(1)

    for i in daily_rate_change.columns.values:
        plt.plot(daily_rate_change.index, daily_rate_change[i], lw=2, label=i)

    plt.title("Volatility")

    plt.xlabel("GAFA_date", fontsize=16)

    plt.ylabel("Daily_Volatillity")

    plt.legend(loc="upper right", fontsize=10)

    plt.show()
