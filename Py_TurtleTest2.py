from logging import root
import turtle
from turtle import Screen, Turtle
from random import random

def stop():
    turtle.bye()

def DrawRainbow2():
    mypen = turtle.Turtle()
    mypen.shape('turtle')
    mypen.speed(15)
    root.protocol("WM_DELETE_WINDOW", stop)
    
    window = turtle.Screen()
    window.bgcolor('white')
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    size = 180
    mypen.penup()
    mypen.goto(0, -180)
    for color in rainbow:
        mypen.color(color)
        mypen.fillcolor(color)
        mypen.begin_fill()
        mypen.circle(size)
        mypen.end_fill()
        size -= 20
    
    turtle.done()

def DrawRainbow1():
    # Creating a turtle screen object
    sc = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True

    # Creating a turtle object(pen)
    pen = turtle.Turtle()
    root.protocol("WM_DELETE_WINDOW", stop)
    
    # Defining a method to form a semicircle
    # with a dynamic radius and color
    def semi_circle(col, rad, val):
        # Set the fill color of the semicircle
        pen.color(col)
    
        # Draw a circle
        pen.circle(rad, -180)
    
        # Move the turtle to air
        pen.up()
    
        # Move the turtle to a given position
        pen.setpos(val, 0)
    
        # Move the turtle to the ground
        pen.down()
    
        pen.right(180)
        
    # Set the colors for drawing
    col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    
    # Setup the screen features
    sc.setup(600, 600)
    
    # Set the screen color to black
    sc.bgcolor('black')
    
    # Setup the turtle features
    pen.right(90)
    pen.width(10)
    pen.speed(7)
    
    # Loop to draw 7 semicircles
    for i in range(7):
        semi_circle(col[i], 10 * (i + 8), -10 * (i + 1))
    
    # Hide the turtle
    pen.hideturtle()

def DrawAxis():
    t1 = Turtle()   # Turtle is a drawer

    # set direction at 0
    # angle using seth
    t1.seth(0) 
    
    # motion 
    t1.forward(80) 
    t1.write("East") 
    
    # back to home 
    t1.home() 
    
    # set direction at 90 
    # angle using sethading 
    t1.setheading(90) 
    
    # motion 
    t1.forward(80) 
    t1.write("North") 
    
    # back to home 
    t1.home() 
    
    # set direction at 180 
    # angle using seth 
    t1.seth(180) 
    
    # motion 
    t1.forward(80) 
    t1.write("West",align="right") 
    
    # back to home 
    t1.home() 
    
    # set direction at 270 
    # angle using setheading 
    t1.setheading(270) 
    
    # motion 
    t1.forward(80) 
    t1.write("South") 
    
    # hide the turtle 
    t1.ht()
    t1.screen.mainloop()

def DrawRectanlge():
    t2 = Turtle()   # Turtle is a drawer

    t2.forward(100) # Draw a line
    t2.right(90)    # Direction to Right
    t2.forward(100) # Draw a line
    t2.right(90)    # Direction to Right
    t2.forward(100) # Draw a line
    t2.right(90)    # Direction to Right
    t2.forward(100) # Draw a line

    t2.clear()

    t2.forward(50)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(50)

    t2.screen.mainloop()

def Draw1():
    t3 = Turtle()   # Turtle is a drawer

    for steps in range(100):
        for c in ('blue', 'red', 'green'):
            t3.color(c)
            t3.forward(steps)
            t3.right(30)

    t3.screen.mainloop()

def Draw2():
    t4 = Turtle()   # Turtle is a drawer

    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t4.right(angle)
        t4.fd(steps)

    t4.screen.mainloop()


# Main Program
#DrawRectanlge()
#DrawAxis()
#Draw1()
#Draw2()
DrawRainbow2()
DrawRainbow1()
