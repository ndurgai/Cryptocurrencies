# Last Updated: 05/07. This module contains functions whjch calculate the Historical VaR for both single assets
# and for multi asset portfolios.
import numpy as np

def historicalSingleVaR(cleanasset, confidence):
    """Given a distribution of returns and a validity period T, this function calculates the historical VaR for a single
    asset. """
    negVaR = np.percentile(cleanasset, 100-confidence)  # returns the 100-confidence percentile
    if negVaR < 0:
        VaR = abs(negVaR)
    else: VaR = 0
    return VaR

def historicalSingleCVaR(cleanasset, confidence):
    """Given a distribution of returns and a validity period T, this function calculates the historical CVaR for a
    single asset. CVaR is 0 if VaR is positive. """
    negVaR = np.percentile(cleanasset, 100-confidence)  # returns the 100-confidence percentile
    if negVaR < 0:
        sortedReturns = np.sort(cleanasset)
        upperIndex = np.round((len(sortedReturns)/100) * (100-confidence))
        totalCVaR = 0
        for index in range(upperIndex):
            totalCVaR += sortedReturns[index]
        CVaR = totalCVaR / len(sortedReturns)
    else: CVaR = 0
    return CVaR

def historicalPortfolioVaR(cleandata, confidence, weights):
    """Calculates historical VaR for a given portfolio assuming the windwowsize is the dataset length """
    returnslist = []
    cleandata2 = np.asarray(cleandata)
    weight2 = np.asarray(weights)
    for row in cleandata2:
        rowreturn = np.dot(weight2,row)
        returnslist.append(rowreturn)
    negVaR = np.percentile(returnslist, 100 - confidence)  # returns the 100-confidence percentile
    if negVaR < 0:
        VaR = abs(negVaR)
    else: VaR = 0
    return VaR

def historicalPortfolioCVaR(cleandata, confidence, weights):
    """Calculates historical CVaR for a given portfolio """
    returnslist = []
    cleandata2 = np.asarray(cleandata)
    weight2 = np.asarray(weights)
    for row in cleandata2:
        rowreturn = np.dot(weight2,row)
        returnslist.append(rowreturn)
    negVaR = np.percentile(returnslist, 100 - confidence)  # returns the 100-confidence percentile
    if negVaR < 0:
        sortedReturns = np.sort(returnslist)
        upperIndex = np.round((len(sortedReturns)/100) * (100-confidence))
        totalCVaR = 0
        for index in range(upperIndex):
            totalCVaR += sortedReturns[index]
        CVaR = totalCVaR / len(sortedReturns)
    else: CVaR = 0
    return CVaR