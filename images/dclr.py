#############################################################
# Program Name: dclr                                        #
# Date: 2020-08-27                                          # 
# Descrption: Draw a star with color                        #
# Author: AceITnow                                          #
#############################################################

def drawStar(numSides):
    import turtle
    myTurtle = turtle.Turtle()
    turnAngle = 144
    col = "red"
    myTurtle.begin_fill()
    myTurtle.down()
    for i in range(numSides):
        sideLength = 150
        myTurtle.color(col)
        myTurtle.forward(sideLength)   # draw line
        myTurtle.left(turnAngle)       # turn 144 degrees
    myTurtle.up()
    myTurtle.end_fill()
        
