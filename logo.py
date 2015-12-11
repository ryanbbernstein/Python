# coding: utf-8
import PIL
from PIL import Image
from PIL import ImageOps
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print filename

img = Image.open(filename)
wpercent = (600 / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((600, hsize), PIL.Image.ANTIALIAS)
img.save("logo600.jpg")

img = Image.open(filename)
hpercent = (100 / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, 100), PIL.Image.ANTIALIAS)
w = int(640 - img.size[0])
img = ImageOps.expand(img, border = w, fill = "#ffffff")
img = ImageOps.fit(img, (640, 100), 0, 0, (0.5,0.5))
img.save("logo640x100.jpg")