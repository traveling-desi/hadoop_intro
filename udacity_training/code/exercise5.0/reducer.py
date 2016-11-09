#!/usr/bin/python

import sys

salesTotal = 0.0
oldKey = None
numSales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)


    if oldKey and oldKey != thisKey:
	meanSales = salesTotal/numSales
        print oldKey, "\t", meanSales
        salesTotal = 0.0
	numSales = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    numSales += 1	

if oldKey != None:
    meanSales = salesTotal/numSales
    print oldKey, "\t", meanSales
