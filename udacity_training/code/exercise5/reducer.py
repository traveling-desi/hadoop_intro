#!/usr/bin/python

import sys

oldKey = None
printList = []
thisLine = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

(reputation, gold, silver, bronze) = (0, 0, 0, 0)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #print len(data_mapped), type(data_mapped), data_mapped
    if len(data_mapped) < 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisLine = data_mapped[0], data_mapped[1:]

    #print thisKey, thisLine
    #print int(data_mapped[0]), type(data_mapped[0]), data_mapped[1:], len(data_mapped[1:])

    if oldKey != None and oldKey != thisKey:
    	#print "-" * 100
	for i in printList:
		print '\t'.join(i),  reputation , gold , silver , bronze
	printList = []
	(reputation, gold, silver, bronze) = (0, 0, 0, 0)

    oldKey = thisKey

    if thisLine[0] == 'A':
	#print "HERE"
	(reputation, gold, silver, bronze) = thisLine[2:6]
    else:
	#(id, title, tagnames, author, node_type, parent_id, abs_parent_id, added_at, score) = data[0:9]
	printList.append(thisLine[1:])
