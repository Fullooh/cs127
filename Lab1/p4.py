#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.pensize(5)
t.shape("circle")

for i in range(4):
    t.pencolor("green")
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.pencolor("blue")
    t.left(100)
    t.left(90)

wn.exitonclick()