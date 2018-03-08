import gdax
import csv

public_client = gdax.PublicClient()

def getHistoricGdaxData(currencies, starttime, endtime, granularity):
    """This function obtains historic data for a specified list of pairings of currencies, a start datetime, end
    datetime, and granularity (measured in seconds). The datetimes must be in ISO 8601 standard
    (e.g. '2018-02-06T15:00:01') """

    for currencypair in currencies:
        x = public_client.get_product_historic_rates(currencypair, start=starttime, end=endtime,
                                                     granularity=granularity)
        x.reverse()
        with open(currencypair+'.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(x)

######################################################################################################################
# This script below reads and saves data from gdax over a 3 day history with an hourly frequency

currencies = ['ETH-EUR', 'BTC-EUR', 'ETH-BTC']
startime = '2018-03-02T15:00:01'
endtime = '2018-03-05T15:00:01'
granularity= '3600'
getHistoricGdaxData(currencies, startime, endtime, granularity)

#######################################################################################################################