#!/usr/bin/python

import sys

oldKey = None
#maxHrList = dict()
#maxHrKey = []
#qLen = 0
#aLen = []
#times = 0
items = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

#strList = [""] * 10
#lengthList = [0]*10


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 2:
    #if len(data_mapped) < 3:
        # Something has gone wrong. Skip this line.
	continue

    #thisKey, thisType, thisLen = data_mapped
    #print thisKey, thisType, thisLen
    #print thisKey, thisData
    thisKey, thisData = data_mapped
    if oldKey != None and oldKey != thisKey :
	print oldKey, items
	items = []

    oldKey = thisKey
    items.append(thisData)

if oldKey != None:
	print oldKey, items
    

   
##     if oldKey != None and oldKey != thisKey:
##         if times > lengthList[-1]:
##             for i in range(9):
##                 strList[i] = strList[i+1]
##                 lengthList[i] = lengthList[i+1]
##             strList[9] = oldKey
##             lengthList[9] = times
##         elif times > lengthList[0]:
##             for i in range(9):
##                 if times > lengthList[i+1]:
##                     lengthList[i] = lengthList[i+1]
##                     strList[i] = strList[i+1]
##                 else:
##                     lengthList[i] = times
##                     strList[i] = oldKey
##                     break
## 	#print strList
## 	#print lengthList
## 	times = 0
##  
##     oldKey = thisKey
##     times += 1
## 
## if oldKey != None:
##     if times > lengthList[-1]:
## 	    for i in range(9):
##                 strList[i] = strList[i+1]
##                 lengthList[i] = lengthList[i+1]
##             strList[9] = oldKey
##             lengthList[9] = times
##     elif times > lengthList[0]:
##             for i in range(9):
##                 if times > lengthList[i+1]:
##                     lengthList[i] = lengthList[i+1]
##                     strList[i] = strList[i+1]
##                 else:
##                     lengthList[i] = times
##                     strList[i] = oldKey
## 		    break
## 
## for i in range(10):
##     print strList[9-i], lengthList[9-i]

## 
## 
## 
##     if oldKey != None and oldKey != thisKey:
## 	print oldKey, qLen, int(sum(aLen)/max(len(aLen), 0.0000001))
## 	aLen = []
## 
##     oldKey = thisKey  
##     if thisType == 'question':
## 	qLen = int(thisLen)
##     else:
## 	aLen.append(float(thisLen))
## 	
## if oldKey != None:
##     print oldKey, qLen, int(sum(aLen)/max(len(aLen), 0.0000001))
## 

##     if oldKey != None and oldKey != thisKey:
## 
## 	maxHr = 0
## 	for (k, v) in maxHrList.iteritems():
## 		if v > maxHr:
## 			maxHrKey = []
## 			maxHrKey.append(k)
## 			maxHr = v
## 		elif v == maxHr:
## 			maxHrKey.append(k)
## 
## 	print oldKey, '\t', maxHrKey
## 	maxHrList = dict()	
## 
##     oldKey = thisKey
##     if not thisData in maxHrList: 
##     	maxHrList[thisData] = 1
##     else:
##     	maxHrList[thisData] += 1
## 
## 
## if oldKey != None:
##     maxHr = 0
##     for (k, v) in maxHrList.iteritems():
##     	if v > maxHr:
##         	maxHrKey = []
##                 maxHrKey.append(k)
##                 maxHr = v
##         elif v == maxHr:
##                 maxHrKey.append(k)
## 
##     print oldKey, '\t', maxHrKey
## 
