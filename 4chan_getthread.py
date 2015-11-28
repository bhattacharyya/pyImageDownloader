#!/usr/bin/python

###########################################################################################################
#
# This script downloads images and other media files from 4chan threads.
# You only need to have python installed in your machine
# The command line takes two mandatory arguments : channel name & thread (in that order)
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
parser.add_option('--limit', action="store", dest="limit", type="int", default=200)
options, args = parser.parse_args()

if len(sys.argv) < 3:
	print "Not enough arguments \nUsage : python 4chan_getthread.py channel threadnumber\nExample : python 4chan_getthread.py hr 2463159"
	exit()
idtype = ["jpg" , "jpg ", "png" , "png ", "gif", "gif ", "webm", "webm "]
count = 1
k = ""
empty = 1

path = "./"+ sys.argv[1] + str(sys.argv[2])
if not os.path.exists(path):
	os.makedirs(path)
os.chdir(path)

f1 = urllib2.urlopen('http://boards.4chan.org/' + sys.argv[1] + "/thread/" + str(sys.argv[2])  )
words = f1.read().split("\"")
fout = open("temp.txt" , "w")
for k in words:
	fout.write(k)
f1.close()
fout.close()

f2 = open("temp.txt", "r")
for i in words:

	if re.search("^//i.4cdn.+", i) :
		img = i.split("/")

        	if img[2] == "i.4cdn.org":
			if img[4].split()[0] != sys.argv[1]:
				idx = img[4].split(".")
				ext = idx[1][0:3]
                	if len(idx) == 2 and ext in idtype :
				name = idx[0] + "." + ext
				name2 = idx[0][0:-1] + "." + ext

				if os.path.isfile(name) or os.path.isfile(name2) or os.path.isfile(idx[0]) or os.path.isfile(idx[0][0:-1]):
                                        print name, "exists"
					empty = 0
				else:
					command = "wget https://i.4cdn.org/" + sys.argv[1] + "/" + idx[0] + "." + ext
					os.system(command)
					if options.ftype == False:
						os.system("mv "+ name + " " + idx[0])
					count += 1
					if count > options.limit :
						break
if(count > 1):
	print "\nAll Images Downloaded \n"
	os.remove("temp.txt")
        os.chdir("../")
else:
        print "\nNo Image to Download \n"
	os.remove("temp.txt")
        os.chdir("../")
	if empty == 1:
        	os.rmdir(sys.argv[1]+str(sys.argv[2]))
