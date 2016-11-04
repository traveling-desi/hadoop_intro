#!/usr/bin/python

# Format of each line is:
#10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
#%h %l %u %t \"%r\" %>s %b
#

import sys
import re


#regex = re.compile(r"^(?i).*http://www.the-associates.co.uk.*$", re.IGNORECASE)

for line in sys.stdin:
    data = line.strip().split()
#data is
#['10.223.157.186', '-', '-', '[15/Jul/2009:15:50:36', '-0700]', '"GET', '/assets/img/dummy/primary-news-1.jpg', 'HTTP/1.1"', '200', '10556']
    #print data
    if len(data) == 10:
        ip, id, user, date, zone, method, site, protocol, response, size = data
	#site = regex.sub("http://www.the-associates.co.uk %s" % "", site)
	site = site.replace("http://www.the-associates.co.uk", "")
        print "{0}\t{1}".format(site, 1)
        #print "{0}\t{1}".format(ip, 1)

