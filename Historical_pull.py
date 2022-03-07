import requests
import pandas as pd
import numpy
import json
import csv
import yfinance as yf


class Data_Pull:

    def __init__(self, inp):
        try:
            stock = yf.ticker(inp)
        except:
            print("Data cannot be accessed. Most likely an invalid ticker symbol.")

        self.stock = stock
        return

    def check_etf(input):
        # Checks whether the input is a valid etf symbol in the Yahoo! Finance Database
        # Args: The input ticker symbol
        # Effects: Returns bool True if a valid etf, else returns error
        pass

    def data_pull(input, start_year=0, end_year=0):
        # Assumes input is a valid ticker and etf,
        # Pulls data from Yahoo! Finance API in the range of the start and end year
        # If start and end year are not given it defaults to the last 6 months
        # Args: The input ticker symbol
        # Effects: Creates a _____ file storing the pulled data
        pass

    def data_format(input):
        # Takes the data from the _____ file and puts it into a pandas dataframe
        # Args: The input ticker symbol
        # Effects: Creates a pandas data frame storing the pulled data with the ticker symbol and data as the keys.
        pass
