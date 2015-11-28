#!/usr/bin/python

from Tkinter import *

import re
import urllib
import urllib2
import sys
import os

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = Tk()
root.title("Subreddit_Scraper")
ask_label = Label(text = "Enter Subreddit Name", bg="black", fg="white").grid(row = 5, column = 30, pady=10)
ask_label = Label(text = "File Type ?", bg="black", fg="white").grid(row = 5, column = 25)
ask_label = Label(text = "Max Images ?", bg="black", fg="white").grid(row = 5, column = 51, pady=10, padx =10)
root["bg"] = "black"
center(root)

root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(423, 179))

subr_name = StringVar()
subreddit  = Entry(textvariable=subr_name, width = 15).grid(row = 9, column = 30)

num_images = IntVar()
imageLimit = Entry(textvariable=num_images, width=3).grid(row = 9, column = 51, padx=10)
num_images.set(60)

image_ext = StringVar()
imageExtension = Radiobutton(text="No ", variable=image_ext, value="No").grid(row = 9, column = 25, padx=35, pady=15)
imageExtension = Radiobutton(text="Yes", variable=image_ext, value="Yes").grid(row = 10, column = 25, padx=35)
image_ext.set("No")

img = ""

def run():
	inp_text = subr_name.get()
	max_images = num_images.get()
	extension = image_ext.get()

	path = "./"+inp_text
	if not os.path.exists(path):
    		os.makedirs(path)
	os.chdir(path)
	
	count = 1
	k = ""

	f1 = urllib2.urlopen('http://imgur.com/r/' + inp_text)
	words = f1.read().split("\"")

	for i in words:

		if re.search("^//i.imgur.+", i) :
			img = i.split("/")
			# print img

                        if img[2] == "i.imgur.com":
				if img[3][-4:] == ".jpg" :
                        		i = "https://i.imgur.com/" + img[3][:-5] + ".jpg"
				if img[3][-4:] == ".png" :
                                        i = "https://i.imgur.com/" + img[3][:-5] + ".png"
                                # print "new i is : " + i
                        if k != i :
                        	print "fetching ", img[3]
				if extension == "No":
                        		name = inp_text + "-" + str(count) 
				else:
					name = inp_text + "-" + str(count) + img[3][-4:]
                        	urllib.urlretrieve(i, name)
                                count += 1
                         	k = i
				if count > max_images:
					break

	if(count > 1):
		print "\nAll Images Downloaded \n"
		os.chdir("../")
	else:
		print "\nNo Image found for the Subreddit \n"
		os.chdir("../")
		os.rmdir(inp_text)

subr_button = Button(text = "Fetch", command = run).grid(row = 50, column = 30)
root.mainloop()
