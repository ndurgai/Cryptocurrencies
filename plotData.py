import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

def plotSeries(mydata):
    """Plot all of the columns of the time series """
    plt.plot(mydata)
    plt.grid()
    plt.show()

def plotOpen(mydata):
    """Plot the Open price of the time series """
    plt.plot(mydata['Open'])
    plt.show()

def plotBitcoinSeries(mydata, series):
    plt.plot(mydata, marker = 'o')
    plt.grid()
    plt.legend(series)
    plt.show()

def compareNorm(mydata, series, binsize):
    """Plots a histogram of the data with the normal distribution. Default number of bins is 100 """

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


