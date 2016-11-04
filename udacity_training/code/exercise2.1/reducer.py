#!/usr/bin/python

import sys

oldKey = None
numHits = 0

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

    thisKey, thisHit = data_mapped
    thisHit = float(thisHit)

    numHits += 1	

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", numHits
        numHits = 0.0

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", numHits
