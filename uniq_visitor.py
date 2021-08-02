#!/usr/bin/python

import sys
import re

try:
    if sys.argv[1:]:
        print "File:",(sys.argv[1])
        logfile = sys.argv[1]
    else:
        logfile = input("Please enter a log file to parse, e.g /var/log/secure: ")
    try:
        file = open(logfile, "r")
        ips = []
        for text in file.readlines():
            #print (text)
            text = text.rstrip()
            regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
            if regex is not None and regex not in ips:
               #print(regex ,"is not null")
               ips.append(regex)
        print(ips)
        for ip in ips:
           outfile = open("/tmp/list.txt", "a")
           addy = "".join(ip)
           if addy is not '':
              print("IP:" ,addy)
              outfile.write(addy)
              outfile.write("\n")
    finally:
        file.close()
        outfile.close()
except IOError, (errno, strerror):
        print ("I/O Error(",errno,") :" ,strerror)