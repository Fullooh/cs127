#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.pensize(5)
t.shape("circle")

for i in range(1):
    t.pencolor("blue")
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)

    t.pencolor("green")
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)

    t.pencolor("red")
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)

    t.pencolor("cyan")
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)


wn.exitonclick()