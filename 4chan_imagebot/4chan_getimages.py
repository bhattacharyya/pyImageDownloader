#!/usr/bin/python

#imports
from Tkinter import *

import re
import urllib
import urllib2
import sys
import os

#open the window in the center
#adapted for someone else's code

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#Design the Window and place labels
root = Tk()
root.title("4chan_Scraper")
ask_label = Label(text = "Enter Channel Abbr", bg="black", fg="white").grid(row = 5, column = 30, pady=10)
ask_label = Label(text = "File Type ?", bg="black", fg="white").grid(row = 5, column = 25)
ask_label = Label(text = "Thread number", bg="black", fg="white").grid(row = 5, column = 51, pady=10, padx =10)
root["bg"] = "black"
center(root) # Center the window here
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(423, 179))

#Set up user input
subr_name = StringVar()
subreddit  = Entry(textvariable=subr_name, width = 4).grid(row = 9, column = 30)

thread_id = IntVar()
threadId = Entry(textvariable=thread_id, width=14).grid(row = 9, column = 51, padx=10)

image_ext = StringVar()
imageExtension = Radiobutton(text="No ", variable=image_ext, value="No").grid(row = 9, column = 25, padx=35, pady=15)
imageExtension = Radiobutton(text="Yes", variable=image_ext, value="Yes").grid(row = 10, column = 25, padx=35)
image_ext.set("No") # It is recommended not to download images with extensions (jpg/png) hard coded

img = ""

#Engine that gets the images upon button click

def run():
	#Collect the user inputs
	inp_text = subr_name.get()
	thread_num = thread_id.get()
	extension = image_ext.get()

	path = "./"+inp_text+str(thread_num) #New directory to store images
	if not os.path.exists(path):
    		os.makedirs(path)
	os.chdir(path)
	
	#initialize variables
	count = 1 #Image count
	k = "" #Tracks previous filename to prevent multiple downloads

	f1 = urllib2.urlopen('http://boards.4chan.org/' + inp_text + "/thread/" + str(thread_num) )
	words = f1.read().split("\"")

	for i in words:

		if re.search("^//i.4cdn.+", i) :
			img = i.split("/")
			print img

                        if img[2] == "i.4cdn.org":
				if img[4][-4:] == ".jpg" :
                        		i = "http://i.4cdn.org/" + inp_text + "/" + img[4][:-5] + ".jpg"
				if img[4][-4:] == ".png" :
                                        i = "http://i.4cdn.org/" + inp_text + "/" + img[4][:-5] + ".png"
                                print "new i is : " + i
                        if k != i :
                        	print "fetching ", img[4]
				if extension == "No":
                        		name = inp_text + str(thread_num) + "-" + str(count) 
				else:
					name = inp_text + str(thread_num) + "-" + str(count) + img[4][-4:]
				if img[4][-4:] == ".jpg" or img[4][-4:] == ".png" : #Large files like webm leading to timeout
                        		urllib.urlretrieve(i, name)
					if os.path.getsize(name) < 10000: #Checks for dead html rather than image files
						os.remove(name)
                                	count += 1
                         		k = i

	if(count > 1):
		print "\nAll Images Downloaded \n"
		os.chdir("../")
	else:
		print "\nNo Image found for the Subreddit \n"
		os.chdir("../")
		os.rmdir(inp_text)

subr_button = Button(text = "Fetch", command = run).grid(row = 50, column = 30) #The trigger for downloads
root.mainloop()
