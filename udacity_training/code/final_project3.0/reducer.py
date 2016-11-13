#!/usr/bin/python
 
import sys
 
oldKey = None
times = 0
 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
 
strList = [""] * 10
lengthList = [0]*10
 
 
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 2:
    #if len(data_mapped) < 3:
        # Something has gone wrong. Skip this line.
        continue
 
    thisKey, thisData = data_mapped
 
    if oldKey != None and oldKey != thisKey:
        if times > lengthList[-1]:
            for i in range(9):
                strList[i] = strList[i+1]
                lengthList[i] = lengthList[i+1]
            strList[9] = oldKey
            lengthList[9] = times
        elif times > lengthList[0]:
            for i in range(9):
                if times > lengthList[i+1]:
                    lengthList[i] = lengthList[i+1]
                    strList[i] = strList[i+1]
                else:
                    lengthList[i] = times
                    strList[i] = oldKey
                    break
        times = 0
 
    oldKey = thisKey
    times += 1

if oldKey != None:
    if times > lengthList[-1]:
            for i in range(9):
                strList[i] = strList[i+1]
                lengthList[i] = lengthList[i+1]
            strList[9] = oldKey
            lengthList[9] = times
    elif times > lengthList[0]:
            for i in range(9):
                if times > lengthList[i+1]:
                    lengthList[i] = lengthList[i+1]
                    strList[i] = strList[i+1]
                else:
                    lengthList[i] = times
                    strList[i] = oldKey
                    break

for i in range(10):
    print strList[9-i], lengthList[9-i]
