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
                for word in data[2].split():
                        print "{0}\t1".format(word)

