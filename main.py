import historicalVaR
import datetime
import numpy as np
import scipy.stats as st
from numpy import genfromtxt
import pandas as pd
import plotData
import matplotlib.pyplot as plt
import matplotlib
import time
import readData
import getGdaxData
import readGdaxData

def plotGdaxData(unixDatetime, value1, value1Name, value2, value2Name):
    """Currently only plots data which has a common datetime"""
    z = unixDatetime.copy()
    for index in range(len(z)):
        z[index] = datetime.datetime.fromtimestamp(unixDatetime[index])

    pd.DataFrame({
        'Datetime': z,
        value1Name: value1,
        value2Name: value2
    }).plot(x = 'Datetime', title= value1Name + ', ' + value2Name)

    # plt.plot(z, x['Open'], marker = 'o')
    plt.grid()
    plt.show()

######################################################################################################################
# plotGdaxData: This script reads two csv files and plots selected data out of both of them

#x = readGdaxData.readCSV('ETH-EUR.csv')
#y = readGdaxData.readCSV('BTC-EUR.csv')
#plotGdaxData(x['Stamp'], x['Open'],'BTC-Open', y['Open'], 'ETH-Open')

######################################################################################################################




