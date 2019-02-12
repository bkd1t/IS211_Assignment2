#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 2, Task 01"""
import urllib
import csv
from datetime import datetime
import os
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("--url", help="the url for the csv", action="store_true")
parser.add_argument('url', nargs='?', default="")
#_StoreAction(option_strings=[], dest='dir', nargs='?', const=None, default='', type=None, choices=None, help=None, metavar=None)
args = parser.parse_args()
if args.url:
    my_url = args.url
else:
    exit(0)

def downloadData(url):
    """ download the contents located at the ​url.
    """
    raw_data = urllib.urlopen(url).readlines()    
    return raw_data


def processData(raw_data):
    """ process the url data.
    """
    logf = open("errors.log", "w")
    res = {}
    for i,each in enumerate(raw_data):
        if i !=0: 
	    x = each.split(",")
	    try:
	        d = datetime.strptime(x[2].rstrip("\n"), '%d/%m/%Y')
		if d:
		    res.update({int(x[0]):(x[1],d)})
	    except Exception as e:
		logf.write("Error processing line {0} for ID {1}\n".format(str(i+1), str(x[0])))
    return res

def displayPerson(user_input,personData):
    """ display Person data.
    """
    if personData.has_key(user_input):
	name = personData[user_input][0]
	dob = personData[user_input][1].strftime('%Y/%m/%d')
	print "Person #{0} is {1} with a birthday of {2}".format(str(user_input),name, str(dob))
    else:
        print "No user found with that id"
    

def main():
  raw_data = downloadData(my_url)
  personData = processData(raw_data)
  while True:
    user_input = raw_input("Enter something:")
    if int(user_input)>0:
        displayPerson(int(user_input),personData)
    else:
        exit(0)
if __name__== "__main__":
  main()

