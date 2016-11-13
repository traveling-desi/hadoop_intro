#!/usr/bin/python

import sys

oldKey = None
aLen = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 3:
        # Something has gone wrong. Skip this line.
	continue

    thisKey, thisType, thisLen = data_mapped

    if oldKey != None and oldKey != thisKey:
	print oldKey, qLen, int(sum(aLen)/max(len(aLen), 0.0000001))
	aLen = []

    oldKey = thisKey  
    if thisType == 'question':
	qLen = int(thisLen)
    else:
	aLen.append(float(thisLen))
	
if oldKey != None:
   print oldKey, qLen, int(sum(aLen)/max(len(aLen), 0.0000001))



