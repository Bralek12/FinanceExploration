from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime as dt


class DataGenerator:

    saved_tickers = sorted([])
    list_of_objects = []
    concocted_object = pd.DataFrame
    source = ""

    def __init__(self, tickers, start_date=dt.datetime(2006, 1, 1), stop_date=dt.datetime(2016, 1, 1), source="yahoo"):
        self.start_date = start_date
        self.stop_date = stop_date
        self.source = source
        for ticker in tickers:
            self.saved_tickers.append(ticker)

    def read_data(self, ticker):
        return data.DataReader(ticker, self.source, self.start_date, self.stop_date)

    def get_data(self):
        for ticker in self.saved_tickers:
            data_frame = self.read_data(ticker)
            self.list_of_objects.append(data_frame)
        concocted = pd.concat(self.list_of_objects, keys=self.saved_tickers, axis=1)
        concocted.columns.names = ["Bank Ticker", "Stock Info"]
        self.concocted_object = concocted
        return concocted

    def add_ticker(self, ticker):
        self.saved_tickers.append(ticker)
        self.list_of_objects.append(self.read_data(ticker))
        print(ticker + " added. You should get new data!")

    def remove_ticker(self, ticker):
        if ticker in self.saved_tickers:
            self.saved_tickers.remove(ticker)
            print(ticker + " removed. You should get new data!")
        else:
            print(ticker + " is not in the list of tickers!")