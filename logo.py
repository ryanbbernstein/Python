# coding: utf-8
import os
from Tkinter import *
from tkFileDialog import askopenfilename

import PIL
from PIL import ImageOps

def create_folder():
	directory = "/Users/YAPI/Dropbox (YAPI)/YAPI (3)/YAPI/Dental Office Logo's/" + officeName.get()
	print directory
	try:
		os.makedirs(directory)
	except OSError:
		pass
	master.quit()

master = Tk()
Label(master, text="Name of Office").grid(row=0)
Label(master, text="Fill Color").grid(row=1)
officeName = Entry(master)
officeName.grid(row=0, column=1)
color = Entry(master)
color.grid(row=1, column=1)
Button(master, text='Create', command=create_folder).grid(row=3, column=1, sticky=W, pady=4)
mainloop()
filename = askopenfilename()

print filename
if not color.get():
	color = "#FFFFFF"
else:
	color = "#" + color.get()
print color

img = PIL.Image.open(filename)
wpercent = (600 / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((600, hsize), PIL.Image.ANTIALIAS)
img.save("/Users/YAPI/Dropbox (YAPI)/YAPI (3)/YAPI/Dental Office Logo's/" + officeName.get() + "/logo600.png")

img = PIL.Image.open(filename)
hpercent = (100 / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, 100), PIL.Image.ANTIALIAS)
w = (int(640 - img.size[0])/2)
img = ImageOps.expand(img, border = w, fill = color)
img = ImageOps.fit(img, (640, 100), 0, 0, (0.5,0.5))
img.save("/Users/YAPI/Dropbox (YAPI)/YAPI (3)/YAPI/Dental Office Logo's/" + officeName.get() + "/logo640x100.png")