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
	if data[5] == 'question':
		print "{0}\t{1}\t{2}".format(data[0], "question" , str(len(data[4])))
	elif data[5] == 'answer':
		print "{0}\t{1}\t{2}".format(data[7], "answer" , str(len(data[4])))
