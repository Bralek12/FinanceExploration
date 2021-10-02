from dataGenerator import DataGenerator
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns


def print_line():
    print(50 * "-")


# Create DataGenerator object
generator = DataGenerator(["BAC", "C", "GS", "JPM", "MS"], source="stooq")
generator.add_ticker("WFC")
print_line()

# Get data frame from the object
bank_stocks = generator.get_data()
print(bank_stocks.head(5))
print_line()

# What is the max Close price for each bank's stock throughout the time period?
print(bank_stocks.xs(key='Close', axis=1, level='Stock Info').max())
print_line()


# Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock.
def pct_change_data_frame(data_frame_for_pct_change=pd.DataFrame()):
    for ticker in generator.saved_tickers:
        data_frame_for_pct_change[ticker + " returns"] = (bank_stocks[ticker]["Close"].pct_change())
    return data_frame_for_pct_change


returns = (pct_change_data_frame())
print(returns)
print_line()


# Create a pairplot using seaborn of the returns dataframe
sns.pairplot(returns).savefig("plots/pairplot.png")

# Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns.
print("Mininal single day return")
print(returns.idxmin())
print_line()
print("Maximal single day return")
print(returns.idxmax())
print_line()
print("Standard deviation of returns")
print(returns.std())

# Create a distplot using seaborn of the 2015 returns for Morgan Stanley
sns.displot(returns['2015-01-01':'2015-12-31']["MS returns"], bins=100, kde=True).savefig("plots/distplot-MS.png")

# Create a distplot using seaborn of the 2008 returns for CitiGroup
sns.displot(returns['2015-01-01':'2015-12-31']["C returns"], bins=100, kde=True).savefig("plots/distplot-CG.png")
