#!/usr/bin/python

import sys
import csv
from collections import deque
import re
from datetime import datetime
## #import zipimport
## #importer = zipimport.zipimporter('./dateutil.zip')
## #dateutil = importer.load_module('dateutil')
## #from dateutil import parser
## 
previousLine = ""
reader = csv.reader(sys.stdin, delimiter='\t', quoting= csv.QUOTE_ALL, quotechar = '"')

## 
for line in reader:
    data = line
    if len(data) > 4 and re.match('[\d ]+', data[0]):
	#if data[5] == 'question':
	#	print "{0}\t{1}\t{2}".format(data[0], "question" , str(len(data[4])))
	#elif data[5] == 'answer':
	#	print "{0}\t{1}\t{2}".format(data[7], "answer" , str(len(data[4])))
	#id = data[3]
	#print data[8]
  	#print type(data[8].split()[0])
	#hour = datetime.strptime(data[8].split()[1].split(".")[0], "%H:%M:%S").hour
        #hour = parser.parse(data[8]).hour
	#print "{0}\t{1}".format(id, hour)
	#if data[5] == 'question':
	#	for word in data[2].split():
	#		print "{0}\t1".format(word)
	if data[5] == 'question':
		print "{0}\t{1}".format(data[0], data[3])
	elif data[5] == 'answer' or data[5] == 'comment':
		print "{0}\t{1}".format(data[7], data[3])
