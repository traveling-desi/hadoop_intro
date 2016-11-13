#!/usr/bin/python
 
import sys
import csv
from collections import deque
import re
from datetime import datetime
previousLine = ""
reader = csv.reader(sys.stdin, delimiter='\t', quoting= csv.QUOTE_ALL, quotechar = '"')
 
## 
for line in reader:
    data = line
    if len(data) > 4 and re.match('[\d ]+', data[0]):
        if data[5] == 'question':
                print "{0}\t{1}".format(data[0], data[3])
        elif data[5] == 'answer' or data[5] == 'comment':
                print "{0}\t{1}".format(data[7], data[3])

