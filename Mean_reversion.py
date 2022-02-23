import requests
import pandas as pd
import numpy
import json
import csv
import urllib
import Historical_pull

# Goal is to pull stock data over a period of time, calculate trend and strength away from the mean
# Then generate a signal on whether it would make more sense to buy or short the stock, incorporating 
# the previous historical data to increase accuracy of the prediction
