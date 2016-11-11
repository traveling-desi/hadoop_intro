#!/usr/bin/python

import sys

oldKey = None
maxHrList = dict()
maxHrKey = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 2:
        # Something has gone wrong. Skip this line.
	continue

    thisKey, thisData = data_mapped

    if oldKey != None and oldKey != thisKey:

	maxHr = 0
	for (k, v) in maxHrList.iteritems():
		if v > maxHr:
			maxHrKey = []
			maxHrKey.append(k)
			maxHr = v
		elif v == maxHr:
			maxHrKey.append(k)

	print oldKey, '\t', maxHrKey
	maxHrList = dict()	

    oldKey = thisKey
    if not thisData in maxHrList: 
    	maxHrList[thisData] = 1
    else:
    	maxHrList[thisData] += 1


if oldKey != None:
    maxHr = 0
    for (k, v) in maxHrList.iteritems():
    	if v > maxHr:
        	maxHrKey = []
                maxHrKey.append(k)
                maxHr = v
        elif v == maxHr:
                maxHrKey.append(k)

    print oldKey, '\t', maxHrKey

