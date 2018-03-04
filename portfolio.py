import pandas as pd
import numpy as np
import gdax

public_client = gdax.PublicClient()

def getCurrentPortfolio():
    """ This function reads the csv file outlining the current portfolio. """
    df = pd.read_csv('portfolio.csv')
    df.as_matrix()
    return(df)

def getTransactionList():
    """Obtains a list of transactions from a CSV file. "Price" refers to the current price of the bought currency in
    terms of the sold currency. "Size" refers to the volume of the new currency obtained."""
    df = pd.read_csv('transactions.csv')
    df.as_matrix()
    return(df)

def getMarktoMarket():
    """This function obtains the current portfolio and marks to market."""
    x = getCurrentPortfolio()

    # Current Bitcoin Price
    a = public_client.get_product_ticker(product_id='BTC-EUR')['price']
    # Current Ether price
    b = public_client.get_product_ticker(product_id='ETH-EUR')['price']

    currentValue = float(x['BTC'][0])*float(a) + float(x['ETH'][0])*float(b)
    return(currentValue)

def getPortfolioChange(dateTime):
    """For a specified dateTime, this returns a percentage change of the portfolio.
    datetime, and granularity (measured in seconds). The dateTime must be in ISO 8601 standard MINUS THE SECONDS
    (e.g. '2018-02-06T15:00')"""
    c = getCurrentPortfolio()
    currentValue = getMarktoMarket()

    a = public_client.get_product_historic_rates('BTC-EUR', start=dateTime+':00', end=dateTime+':20')[0][1]
    b = public_client.get_product_historic_rates('ETH-EUR', start=dateTime+':00', end=dateTime+':20')[0][1]

    oldValue = float(c['BTC'][0]) * float(a) + float(c['ETH'][0]) * float(b)

    change = ((currentValue-oldValue)/oldValue) * 100
    return(change)

#####################################################################################################################
# getPortfolioChange: This script tests out this function

#r = getPortfolioChange('2018-02-20T15:00')
#print(r)
#####################################################################################################################

x = getMarktoMarket()
print(x)