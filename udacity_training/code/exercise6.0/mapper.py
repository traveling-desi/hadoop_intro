#!/usr/bin/python

import sys
import csv
from collections import deque
import re

previousLine = ""

for line in sys.stdin:
    line = line.replace("\"", "")
    line = line.strip()
    if not re.match('[\d ]+', line):
    	previousLine += line
	continue
    else:
	temp = line
	line = previousLine
	previousLine = temp
    data = line.split("\t")
    if len(data) > 4:
	if "".join(data).isdigit():
		id = data[0]
		print "{0}\t{1}".format(id, 'A' + '\t' + '\t'.join(data))
	else:
		id = data[3]
		print "{0}\t{1}".format(id, 'B' + '\t' +  '\t'.join(['\t'.join(data[0:4]), '\t'.join(data[5:10])]))
