import numpy as np
import pandas as pd


def readCSV(wikifuturescsv):
    """This function reads a specified CSV file and outputs it as a matrix?"""
    df = pd.read_csv(wikifuturescsv)
    df.as_matrix()
    return df

#####################################################################################################################
# Reads a CSV file and prints it out

#x = readCSV('ETH-BTC.csv')
#print(x)
#####################################################################################################################