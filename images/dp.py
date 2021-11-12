#############################################################
# Program Name: dp                                          #
# Date: 2020-08-27                                          # 
# Descrption: Draw a Polygon                                #
# Author: AceITnow                                          #
#############################################################

def drawPolygon(myTurtle,sideLength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)   # draw line
        myTurtle.right(turnAngle)      # turn degrees
