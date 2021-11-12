#############################################################
# Program Name: df                                          #
# Date: 2020-08-27                                          # 
# Descrption: Draw a flower                                 #
# Author: AceITnow                                          #
#############################################################

def drawFlower(numSquares):
    import turtle
    myTurtle = turtle.Turtle()            
    for i in range(numSquares):
        sideLength = 100
        myTurtle.right(30)    # turn 90 degrees
        myTurtle.forward(sideLength)   # draw line
        myTurtle.right(90)    # turn 90 degrees
        myTurtle.forward(sideLength)   # draw line
        myTurtle.right(90)    # turn 90 degrees
        myTurtle.forward(sideLength)   # draw line
        myTurtle.right(90)    # turn 90 degrees
        myTurtle.forward(sideLength)   # draw line
             
