import turtle
from random import randint

myPen = turtle.Turtle()
myWin = turtle.Screen()
myPen.speed(0)

def drawTree(branchLen, t, size):
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
        
        if size<0: 
            size=1
            rsize = size
        else:
            rsize = size + 1
            
        myPen.pensize(size)
        tangle = 20
        t.forward(branchLen)
        t.right(tangle)
        drawTree(branchLen-randint(5, 15),t,size-1)
   
        t.left(2*tangle)
        drawTree(branchLen-randint(5, 15),t,size-1)
        t.right(tangle)
        
        t.backward(branchLen)
        myPen.pensize(rsize)
        t.color("black")
        
#myPen.hideturtle()
myPen.penup()
size = 10
myPen.pensize(size)
myPen.goto(-50,-300)
myPen.pendown()
myPen.left(90)
drawTree(100, myPen, size)
myWin.exitonclick()