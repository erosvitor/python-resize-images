#!/usr/bin/python3

import sys
import os
from PIL import Image

if len(sys.argv) != 5:
  print("Usage:")
  print("  python3 ResizeImages.py <srcdir> <dstdir> <width> <height>")
  print("")
  print("    srcdir = source directory of the images")
  print("    dstdir = target directory of the images resized")
  print("    width  = new width of image")
  print("    heigth = new height of image")
  quit()

srcdir = sys.argv[1]
dstdir = sys.argv[2]

if not os.path.isdir(srcdir):
  print("The source directory '" + srcdir + "' not exist!")
  quit()

if not os.path.isdir(dstdir):
  print("The target directory '" + dstdir + "' not exist!")
  quit()

try:
  newwidth = int(sys.argv[3])
except ValueError:
  print("The " + sys.argv[3] + " is not a valid width")
  quit()

try:
  newheight = int(sys.argv[4])
except ValueError:
  print("The " + sys.argv[4] + " is not a valid height")
  quit()

print("Resizing images from " + srcdir + ". Please wait...")

entries = os.listdir(srcdir)
for entry in entries:
  img = Image.open(srcdir + "/" + entry)
  img = img.resize((newwidth, newheight), Image.ANTIALIAS)
  img.save(dstdir + "/" + entry)

print("Ok. All images resized succesfull")
