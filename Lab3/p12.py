#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import turtle

turtle.colormode(255)
t=turtle.Turtle()

for i in range(0,255,10):
    t.color(i,0,i)
    t.pensize(i)
    t.forward(10)

for i in range(255,0,-10):
    t.color(i,0,i)
    t.pensize(i)
    t.forward(10)