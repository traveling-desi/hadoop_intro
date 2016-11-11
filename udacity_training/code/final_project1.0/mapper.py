#!/usr/bin/python

import sys
import csv
from collections import deque
import re
from datetime import datetime
from dateutil import parser

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
	id = data[3]
	#hour = datetime.strptime(data[8].split()[1].split(".")[0], "%H:%M:%S").hour
        hour = parser.parse(data[8]).hour
	print "{0}\t{1}".format(id, hour)
