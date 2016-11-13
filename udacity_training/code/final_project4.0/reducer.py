#!/usr/bin/python
 
import sys
 
oldKey = None
items = []
 

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) < 2:
        continue
 
    thisKey, thisData = data_mapped
    if oldKey != None and oldKey != thisKey :
        print oldKey, items
        items = []
        
    oldKey = thisKey
    items.append(thisData)
 
if oldKey != None:
        print oldKey, items
