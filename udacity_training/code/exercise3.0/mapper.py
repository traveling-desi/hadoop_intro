#!/usr/bin/python

import sys
import csv
from collections import deque
import re

previousLine = ""

for line in sys.stdin:
    line = line.replace("\"", "")
    line = line.strip()
    if not re.match('\d', line):
    	previousLine += line
	continue
    else:
	temp = line
	line = previousLine
	previousLine = temp
    data = line.split("\t")
    if len(data) > 4:
     	str = data[4]
	id = data[0]
        str = str.replace('\n', '')
        count = str.count(".") + str.count("?") + str.count("!")
        if ( count == 0 ):
        	print "{0}\t{1}".format(str, 1)
        srch = str[-1]
        if ( count == 1 and ( srch == "." or srch == "?" or srch == "!") ):
        	print "{0}\t{1}".format(str, 1)
