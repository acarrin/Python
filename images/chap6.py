#############################################################
# Program Name: 6.1   (pg 184)                              #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: modify session 6.5 create line random colors  #
#							    #
# Execution: Run function drawLine()                        #
#############################################################

from cImage import *
import random
import math

def drawLine():
        myImWin = ImageWin("Line Image" ,300 ,300)
        lineImage = EmptyImage(300 ,300)
        for i in range(lineImage.getHeight()):
                randomred = random.randrange(256)
                randomgreen = random.randrange(256)
                randomblue = random.randrange(256)
                lineImage.setPixel(i,i,Pixel(randomred,randomgreen,randomblue))
                                
        lineImage.draw(myImWin)
        lineImage.save("lineImage.gif")
        myImWin.exitOnClick()


#############################################################
# Program Name: 6.9   (pg 190)                              #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: modify session 6.5 create line random colors  #
#							    #
# Execution: Run function bluePixelChange(bChange)          #
#############################################################

#from cImage import *

def bluePixelChange(bChange):

        r = 256
        g = 256
        b = 256
        
        oldPixel = Pixel(r,g,b)
        newPixel = Pixel(r,g,(b-bChange))

        return newPixel


#############################################################
# Program Name: 6.13   (pg 194)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: modify session 6.5 create line random colors  #
#							    #
# Execution: function negativePixel called by makeNegative  #
#############################################################

#from cImage import *

def negativePixel(oldPixel):
    
    newRed   = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue  = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed,newGreen,newBlue)

    return newPixel

    
#############################################################
# Program Name: 6.13   (pg 194)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: modify session 6.5 create line random colors  #
#							    #
# Execution: function called by generalTransform function   #
#############################################################

#from cImage import *

def makeNegative(imageFile):
    
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Negative Image", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel)
            newIm.setPixel(col, row, newPixel)
            
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


#############################################################
# Program Name: 6.13   (pg 194)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: Takes an image and creates a new image        #
# by applying the rgbFunction parameter                     #
#							    #
# Execution: pixelMapper called by generalTransForm         #
#############################################################

#from cImage import *

def pixelMapper(fileImage,rgbFunction):
    
    # Find the width and height of the original image and make
    # a new image that is the same size.
    
    width  = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm  = EmptyImage(width, height) 

    for row in range(height):
            for col in range(width):
                    oldPixel = fileImage.getPixel(col, row)
                    newPixel = rgbFunction(oldPixel)
                    newIm.setPixel(col, row, newPixel)

    return newIm


#############################################################
# Program Name: 6.13   (pg 194)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: modify session 6.5 create line random colors  #
#							    #
# Execution: generalTransform is our main function          #
#############################################################

#from cImage import *

def generalTransform(imageFile):
    
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("Negative Image", width * 2, height)
    oldImage.draw(myImageWindow)
    
    newIm = pixelMapper(oldImage, makeNegative)

    
    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()


#############################################################
# Program Name: 6.27   (pg 212)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: This is a horizontalFlip (top to bottom)      #
#							    #
# Execution: run function with image parameter              #
# img= FileImage("thor_small.gif")                          #
#                                                           #
#############################################################


def horizontalFlip(oldImage):

    
    width = oldImage.getWidth()          
    height = oldImage.getHeight()
    newIm = EmptyImage(width,height)
    # Bottom row number.
    maxRow = height-1

    # Create the image window
    myImageWindow = ImageWin("Flipped Image", width * 2, height)

    for row in range(height):
        for col in range(width):
            # Grab the original pixel in the top-down opposite row.
            originalPixel = oldImage.getPixel(col,maxRow-row)
            # Put it in the current spot in the new image.
            newIm.setPixel(col,row,originalPixel)

    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()
    


#############################################################
# Program Name: 6.37   (pg 194)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: transform colors to grayPixels                #
#							    #
# Execution: function called by edgeDetect                  #
#############################################################

#from cImage import *
#import math

def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + \
                   oldpixel.getBlue()
    aveRGB = intensitySum // 3

    newPixel = Pixel(aveRGB,aveRGB,aveRGB)
    return newPixel


#############################################################
# Program Name: 6.37   (pg 218)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: Convolution function                          #
#							    #
# Execution: function called by edgeDetect                  #
#############################################################


def convolve(anImage,pixelRow,pixelCol,kernel):

    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1
    filterWidth  = 3
    filterHeight = 3
    factor = 1.0 
    bias = 0.0
    
    rsum = 0
    gsum = 0
    bsum = 0
    
    for row in range(kernelRowBase,kernelRowBase+filterWidth):
        for col in range(kernelColumnBase,kernelColumnBase+filterHeight):
            kColIndex = col-kernelColumnBase
            kRowIndex = row-kernelRowBase
            
            apixel = anImage.getPixel(col,row)
            rintensity = apixel.getRed()
            gintensity = apixel.getGreen()
            bintensity = apixel.getBlue()
            
            rsum = rsum + rintensity * kernel[kRowIndex][kColIndex]
            gsum = gsum + gintensity * kernel[kRowIndex][kColIndex]
            bsum = bsum + bintensity * kernel[kRowIndex][kColIndex]

    red = min(max(int((factor * rsum) + bias), 0), 255)
    green = min(max(int((factor * gsum) + bias), 0), 255)
    blue = min(max(int((factor * bsum) + bias), 0), 255)
    return red, green, blue

#############################################################
# Program Name: 6.37   (pg 218)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: Edge Detection Listing 6.13                   #
#							    #
# Execution: run function with image parameter              #
# img= FileImage("thor_small.gif")                          #
#                                                           #
#############################################################

#import math

def edgeDetect(theImage):
    grayImage = pixelMapper(theImage,grayPixel)    
    newim = EmptyImage(grayImage.getWidth(), grayImage.getHeight())
    black = Pixel(0,0,0)
    white = Pixel(255,255,255)
    xMask = [ [-1,-2,-1],[0,0,0],[1,2,1] ]
    yMask = [ [1,0,-1],[2,0,-2],[1,0,-1] ]      

    for row in range(1,grayImage.getHeight()-1):    
        for col in range(1,grayImage.getWidth()-1):   
            gx = convolve(grayImage,row,col,xMask)  
            gy = convolve(grayImage,row,col,yMask)
            g = math.sqrt(gx**2 + gy**2) 
            
            if g > 175:
                newim.setPixel(col,row,black)
            else:
                newim.setPixel(col,row,white)

    return newim


#############################################################
# Program Name: 6.37   (pg 218)                             #
#							    #
# Date: 2020-10-23                                          #
#							    #
# Descrption: applyBlur Function                            #
#							    #
# Execution: run function with image parameter              #
# img= FileImage("thor_small.gif")                          #
#                                                           #
#############################################################

def applyBlur(theImage):

    blurMask = [[1,2,1],[2,1,2],[1,2,1]]
    filterWidth  = 3
    filterHeight = 3
    
    myImageWindow = ImageWin("Blurred Image", theImage.getWidth(),theImage.getHeight())
    newIm = EmptyImage(theImage.getWidth(), theImage.getHeight())
    ignore = filterWidth - 2
    
    for row in range(1,theImage.getHeight()-ignore):    
        for col in range(1,theImage.getWidth()-ignore):
            red,green,blue = convolve(theImage, row, col, blurMask)
            newIm.setPixel(col,row,Pixel(red,green,blue))

    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


    
        
