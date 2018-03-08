import numpy as np
import pandas as pd
from datetime import date, timedelta
import csv

def readRawBitcoinAlerts():
    """ This function reads the csv file containing the raw pasted text from a Google alert. """
    df = pd.read_csv('rawBitcoinAlerts.csv')
    x = np.asarray(df)
    y = [item for sublist in x for item in sublist]
    return(y)

def parseRawAlerts():
    """ This function parses the raw csv file and adds to the csv file of cleaned up alerts"""
    raw = readRawBitcoinAlerts()
    clean = []

    # List of default parameters
    typeList = ("NEWS", "BLOGS", "WEB", "VIDEO", "DISCUSSIONS", "FINANCE", "BOOKS")
    repList = []  # List which contains tuples which contain the index of the clean row and the "Hits -1" value
    skipList = [] # List which contains the indices which are to be skipped over in the main iteration

    global dateRecord
    global type
    global hits

    dateRecord = date.today()
    print(dateRecord)
    type = "NEWS"
    hits = 0
    # Generate repList
    for entry in enumerate(raw):
        if entry[1] == "Full Coverage":
            flag = False
            index = entry[0]
            counter = 1

            while flag == False:
                index = index - 1
                counter = counter + 1
                if "..." in raw[index - 1]:
                    flag = True
                    repList.append((index - 3, counter))

    # Generate skipList
    for entry in repList:
        for x in range(entry[0] + 3, entry[1] + entry[0] + 3):
            skipList.append(x)

    # Main loop which identifies and records entries

    global record
    record = [dateRecord, type, hits] # Min size 3, max size 6]


    for entry in enumerate(raw):

        #Check if end of spreadsheet is reached
        if entry[1] == "Help center":
            break

        #Skip over the first 2 cells as they are meaningless
        if entry[0] == 0 or entry[0] == 1:
            continue

        #Skip over cells in the skipList
        if entry[0] in skipList:
            continue

        #Check if cell is that of a parameter
            #Type
        if entry[1] in typeList:
            record[1] = entry[1]
            continue

            #Date
        elif entry[1] == "1 day ago":
            record[0] = date.today() - timedelta(1)
            continue
        elif entry[1] == "2 days ago":
            record[0] = date.today() - timedelta(2)
            continue
        elif entry[1] == "3 days ago":
            record[0] = date.today() - timedelta(3)
            continue

            # Hits
        if entry[0] in dict(repList).keys():
        # Else add record to the "records" list as it must be a
            record[2] = dict(repList)[entry[0]] - 1

        record.append(entry[1])

        if len(record) == 6:
            clean.append(record.copy())
            del record[len(record)-1]
            del record[len(record) - 1]
            del record[len(record) - 1]

    clean.reverse()

    with open('bitcoinAlerts.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(clean)

#################################################################
parseRawAlerts()









