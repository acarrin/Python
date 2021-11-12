#############################################################
# Program Name: dstar                                       #
# Date: 2020-08-27                                          # 
# Descrption: Draw a star restricted to odd # points        #
# Author: AceITnow                                          #
#############################################################

def drawStar(numPoints):
    import turtle
    myTurtle = turtle.Turtle()
    turnAngle = 144
    if numPoints % 2 == 0:
        print ("The number of Star Points must be an odd number")
    else:
        for i in range(numPoints):
            sideLength = 150
            myTurtle.forward(sideLength)   # draw line
            myTurtle.left(turnAngle)       # turn 144 degrees
        
