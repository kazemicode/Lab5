import random 
# Sara Kazemi
# Lab5

# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = "/Documents/CST205/Lab5/output/"

## main method
def main():
  makeCollage(2550, 3300, 8)
# 2550 is the width, 3330 is the height, and 8 is the number of pics in the collage



# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  
##################
# Warmup
##################
 
# Makes a copy of a given picture on to the middle of a larger canvas
def simpleCopy(inPic):
  mypic = makeEmptyPicture(int(getWidth(inPic) * 1.5), int(getHeight(inPic) * 1.5))
  for x in range (0, getWidth(inPic)):
    for y in range (0, getHeight(inPic)):
      setColor(getPixel(mypic, x + int(getWidth(inPic) / 4), y + int(getHeight(inPic)/4)), getColor(getPixel(inPic, x, y)))
  show(mypic)
  return mypic 

##################
# Problem 1
##################

# Generalized solution to making a copy of a given picture on to the middle of a larger canvas 
def pyCopy(source, target, targetX, targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      setColor(getPixel(target, targetX + x, targetY + y), getColor(getPixel(source, x, y)))
  #show(target)
  return target

# Function that applies a random effect on a given picture
def getRandomEffect(pic):
  n = random.randint(0,9)
  #print n
  if n == 0:
    makeNegative(pic)
  elif n == 1:
    QuadMirror(pic)
  elif n == 2:
    roseColoredGlasses(pic)
  elif n == 3:
    betterBnW(pic)
  elif n == 4:
    makeNegative(pic)
  elif n == 5:
    mirrorBottomToTop(pic)
  elif n == 6:
    mirrorTopToBottom(pic)
  elif n == 7:
    mirrorVerticalR(pic)
  elif n == 8:
    noBlue(pic)
  elif n == 9:
    lessRed(pic, 100)
  else:
    return pic
# Function that adds text to the bottom of collage
def addWaterMark(picture, x, y):
  c = makeColor(255, 255, 0)
  s = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(picture, x, y, "Sara Kazemi", s, c) 
  return picture
  


# Problem 2
################################################################
# Make a collage that is 2550 px by 3300 px
# Using images that are all 1024 px by 768 px, we can fit
# 2 photos across, 4 photos up and down on to the canvas
################################################################
def makeCollage(width, height, num_pics):

  collage = makeEmptyPicture(width, height)
  setAllPixelsToAColor(collage, makeColor(100,100,100))
  
  # Build a list of Picture objects
  pics = list()
  for num in range(num_pics):
    pics.append(getPic())
 
  h = getHeight(pics[0])   # height of pics in collage
  w = getWidth(pics[0])    # width of pics in collage
  x_border= int((width - w*2))/2
  y_border = int((height - h*4))/2
  x = x_border             # x coordinate to draw pic
  y = y_border             # y coordinate to draw pic
  p = 0                    # counter for pictures drawn
  for pic in pics:
    getRandomEffect(pics[p])
    if x > x_border + getWidth(pics[p]):
      y += getHeight(pics[p])
      x = x_border
    writePict(pyCopy(pics[p], collage, x, y), dir + "collage.jpg")
    x += getWidth(pics[0])
    p+=1
 
  writePict(addWaterMark(collage, x_border, height - y_border / 2), dir + "collage_with_wm.jpg") 


#########################################################
# Image Modification functions from previous labs below
#########################################################


# Mirror an image vertically, left to right      
def mirrorVerticalL(picture):
  
  for x in range(0, int(getWidth(picture)/2)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
 # show(picture)
  return(picture)
  
# Mirror an image vertically, right to left       
def mirrorVerticalR(picture):
  
  for x in range(int(getWidth(picture)/2), getWidth(picture)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
  #show(picture)
  return(picture)
    

# Mirror an image horizontally, bottom to top        
def mirrorBottomToTop(picture):
  
  for x in range(0, getWidth(picture)):
    for y in range(getHeight(picture)/2 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
 # show(picture)
  return(picture)
  
# Mirror an image horizontally, top to bottom      
def mirrorTopToBottom(picture):
  
  for x in range(0, getWidth(picture)):
    for y in range(0 , getHeight(picture)/2):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
 # show(picture)
  return(picture)

# Mirror an image vertically and horizontally 
def QuadMirror(picture):
   ## mirror vertically, right to left
  for x in range(int(getWidth(picture)/2), getWidth(picture)):
    for y in range(0 , getHeight(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(picture, getWidth(picture) - x - 1, y), color)
   ## mirror horizontally, top to bottom
  for x in range(0, getWidth(picture)):
      for y in range(0 , getHeight(picture)/2):
        color = getColor(getPixel(picture, x, y))
        setColor(getPixel(picture, x, getHeight(picture) - y - 1), color)
  
 # show(picture)
  return(picture)

# Makes a copy of a given picture
def simpleCopy(inPic):
  mypic = makeEmptyPicture(getWidth(inPic), getHeight(inPic))
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), getColor(getPixel(inPic, x, y)))
 # show(mypic)
  return mypic 


# Rotates a picture 90 degrees to the left
def rotatePic(inPic):
  # Swap width and height
  pic = makeEmptyPicture(getHeight(inPic), getWidth(inPic))
  for y in range (0, getHeight(mypic)):
    for x in range (0, getWidth(mypic)):
      setColor(getPixel(pic, x, y), getColor(getPixel(inPic, y, x)))
  #show(pic)
  return pic

# Shrinks a picture by half
def shrink(inPic):
  SHRINK_SIZE = 2 ## shrinking by half
  mypic = makeEmptyPicture(int(getWidth(inPic)/ SHRINK_SIZE), int(getHeight(inPic)/SHRINK_SIZE))
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), getColor(getPixel(inPic, x*SHRINK_SIZE, y*SHRINK_SIZE)))
 # show(pic)
  return pic
  
# Eliminates all blue in each pixel        
def noBlue(pic):
   pixels = getPixels(pic)
   for p in pixels:
    b = getBlue(p)
    setBlue(p, 0)
   #show(pic)
   return pic
    

# Reduces amount of redness by the percentage passed in to the parameter        
def lessRed(pic, percent):

   pixels = getPixels(pic)
   for p in pixels:
     r = getRed(p)
     newRed = r - (r * (percent/100))
  
     # set red value to the new reduced value
     setRed(p, newRed)
   #show(pic) 
   return pic
    

# Increases amount of redness by the percentage passed in to the parameter      
def moreRed(percent):
   pixels = getPixels(pic)
   ColorWrapAround(0)
   for p in pixels:
    r = getRed(p)
    newRed = r + (r * (percent/100))
    # The commented lines below aren't needed since ColorWrapAround 
    # is set to false by default to prevent overflow
    #if newRed > 255:
    # newRed = 255
    setRed(p, newRed)
   #show(pic) 
   return pic

# Makes an image appear pink
def roseColoredGlasses(pic):
   pixels = getPixels(pic)
   for p in pixels:
     myRed = getRed(p) 
     myGreen = getGreen(p) * .50
     myBlue = getBlue(p) * .75
     setColor(p, makeColor(myRed, myGreen, myBlue))
   #show(pic) 
   return pic


# Makes every pixel in the picture appear lighter; effectively lightens the entire picture
def lightenUp(pic):
   pixels = getPixels(pic)
   for p in pixels:
    # set color of each pixel to a lighter hue
    setColor(p, makeLighter(getColor(p)))
  # show(pic) 
   return pic


# Alters the picture so that it is the negative of the original
def makeNegative(pic):

   pixels = getPixels(pic)

   for p in pixels:
    # Find opposite of color by subtracting from max
     r = 255 - getRed(p) 
     g = 255 - getGreen(p) 
     b = 255 - getBlue(p)
     setColor(p, makeColor(r, g, b))
   #show(pic)
   return pic


# Alters the picture so that it is grayscale
def BnW(pic):
   pixels = getPixels(pic)
   setColorWrapAround(1)
   for p in pixels:
    # Find opposite of color by subtracting from max
     newColor =  (getRed(p) + getGreen(p) + getBlue(p)) / 3
     setColor(p, makeColor(newColor, newColor, newColor))
  # show(pic)
   return pic
 
# improved grayscale function using weights  
def betterBnW(pic):
   pixels = getPixels(pic)
   setColorWrapAround(1)
   for p in pixels:
      # Find opposite of color by subtracting from max and multiply by weight
      newColor =  (getRed(p) * 0.299 + getGreen(p) * 0.587 + getBlue(p) * 0.114) / 3
      setColor(p, makeColor(newColor, newColor, newColor))
  # show(pic)
   return pic
