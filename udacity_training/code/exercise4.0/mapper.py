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
	for word in re.split("[\s/.,!?:;\"()<>\[\]\#$=-]+", str):
		word = word.strip().lower()
		print "{0}\t{1}".format(word, id)
