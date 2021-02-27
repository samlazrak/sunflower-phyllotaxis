import math
import turtle
import random

t = turtle.Turtle()
t.shape("circle")
window=turtle.Screen()
window.bgcolor("black")
t.speed(100)

def drawPhyllPattern(turtle, t, petalstart, angle=137.5077641, size=15, cspread=5):
    phi = angle * (math.pi / 180.0)
    xcenter = 0.0
    ycenter = 0.0

    for n in range(0, t):
        if n<=50:
            turtle.fillcolor("#7F4313")
        elif n>50 and n<=150:
            turtle.fillcolor("#F2BF41")
        elif n>150 and n<200:
            turtle.fillcolor("#F5CE45")
        r = cspread * math.sqrt(n)
        theta = n * phi
        x = r * math.cos(theta) + xcenter
        y = r * math.sin(theta) + ycenter
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.setheading(n * angle)
        if n > petalstart - 1:
            drawPetal(turtle, x, y)
        else:
            turtle.stamp()

def pick_color():
    colors = ["#7F4313","#F2BF41","#F5CE45"]
    random.shuffle(colors)
    return colors[0]

def drawPetal(turtle, x, y):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    random_color = pick_color()
    turtle.fillcolor(random_color)
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.left(140)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.penup()
    turtle.end_fill()

drawPhyllPattern(t, 250, 200, 137.5077641)
t.penup()
turtle.mainloop()
