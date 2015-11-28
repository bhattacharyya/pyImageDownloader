#!/usr/bin/python

###########################################################################################################
#
# This script downloads images (latest) from a twitter account.
# You only need to have python installed in your machine
# The command line takes one mandatory arguments : twitter account name
# Optional arguments are --ftype (yes or no) that appends the file type to file name (not recommended)
# and --limit (integer) that limits the number of downloaded files to save space or bandwidth
#
# Author : Shantanu S. Bhattacharyya
# Date : Nov 27, 2015
#
############################################################################################################

import re
import urllib
import urllib2
import sys
import os

import optparse
parser = optparse.OptionParser()

parser.add_option('--ftype', action="store_true", default=False)
parser.add_option('--limit', action="store", dest="limit", type="int", default=100)
options, args = parser.parse_args()

if len(sys.argv) < 2:
        print "Not enough arguments \nUsage : python twitter_getpics.py name\n"
        exit()

idtype = ["jpg" , "jpg ", "png" , "png ", "gif", "gif ", "webm", "webm "]
count = 1
k = ""
empty = 1

path = "./"+ sys.argv[1]
if not os.path.exists(path):
	os.makedirs(path)
os.chdir(path)

f1 = urllib2.urlopen('http://twitter.com/' + sys.argv[1] + '/media' )
words = f1.read().split("\"")
fout = open("temp.txt" , "w")
for k in words:
	fout.write(k)
f1.close()
fout.close()

f2 = open("temp.txt", "r")
lines = f2.readlines()
for i in lines:
	img = i.split("/")
	if len(img) == 5 :	
        	if img[2] == "pbs.twimg.com":
			if img[4].split()[0] != sys.argv[1]:
				idx = img[4].split(".")
				print idx ,img
				ext = idx[1][0:3]
                	if len(idx) == 2 and ext in idtype :
				name = idx[0] + "." + ext
				name2 = idx[0][0:-1] + "." + ext

				if os.path.isfile(name) or os.path.isfile(name2) or os.path.isfile(idx[0]) or os.path.isfile(idx[0][0:-1]):
                                        print name, "exists"
					empty = 0
				else:
					command = "wget https://pbs.twimg.com/media/" + idx[0] + "." + ext
					os.system(command)
					if options.ftype == False:
						os.system("mv "+ name + " " + idx[0])
					count += 1
					if count > options.limit :
						break
if(count > 1):
	print "\nAll Images Downloaded \n"
        os.chdir("../")
else:
        print "\nNo Image to Download \n"
        os.chdir("../")
	if empty == 1:
        	os.rmdir(sys.argv[1])
