# Last Updated: 05/07. This module contains functions whjch plot time series and VaR data.

import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# Plot all of the columns of the time series
def plotSeries(mydata):
    plt.plot(mydata)
    plt.grid()
    plt.show()

# Plot the Open price of the time series
def plotOpen(mydata):
    plt.plot(mydata['Open'])
    plt.show()

def plotBitcoinSeries(mydata, series):
    plt.plot(mydata, marker = 'o')
    plt.grid()
    plt.legend(series)
    plt.show()

# Plots a histogram of the data with the normal distribution. Default number of bins is 100
def compareNorm(mydata, series, binsize):
    # Fit a normal distribution to the data:
    mydata2 = np.array(mydata)
    mu, std = st.norm.fit(mydata2)
    # Plot the histogram.
    plt.hist(mydata2, bins=binsize, normed=True, alpha=0.6, color='g')

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = st.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.show()


