"""lab5.ipynb

Original file is located at
    https://colab.research.google.com/drive/1vCb47T7BP20Fa6nIw_y_0PoaGIQs0eq3
"""

#Name: Long Hoang
#Lab 5
#Project idea: convert RGB image to Black and White film-like image

"""Apply black and white filter"""

from PIL import Image, ImageEnhance
import os

#get current working directory: use for getting input file and save output file
cwd = os.path.dirname(__file__)
#print(cwd)

def bnw(r, g, b):
  #gray scale function (The RGB values are converted to grayscale)
  return int(0.299 * r + 0.587 * g + 0.114 * b)

def conversion(input_path, output_path):
  #Open image
  img = Image.open(input_path)

  #assign dimensions
  width, height = img.size

  #Create resulting image: L indicates grayscale image
  bnw_img = Image.new("L", (width, height))

  #Change color code of each pixel using grayscale formula function
  for x in range(width):
    for y in range(height):
      r, g, b = img.getpixel((x, y))
      bnw_img.putpixel((x, y), bnw(r, g, b))

  #Slight edit to enhance image
  #increase contrast
  contrast = ImageEnhance.Contrast(bnw_img)
  bnw_img = contrast.enhance(2)

  #increase brightness
  brightness = ImageEnhance.Brightness(bnw_img)
  bnw_img = brightness.enhance(2)

  #save image
  bnw_img.save(output_path)

  return bnw_img

#input image path
input_path = cwd + "/image.jpg"
output_path = cwd + "/bnw_image.jpg" #output the photo in the current working dir

#Convert image
img = conversion(input_path, output_path)

#show image in the current directory onto your computer
img.show()