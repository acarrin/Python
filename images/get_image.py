#############################################################
# Program Name: 6.4   (pg 184)                              #
#							    #							#
# Date: 2020-10-23                                          #
#							    #							#
# Descrption: Get an image and display it                   #
#							    #					#
# Author: AceITnow                                          #
#############################################################

from cImage import *


myWin = ImageWin("Thor",300, 300)
thor  = FileImage("thor_small.gif")
thor.draw(myWin)                  
