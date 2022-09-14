#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

import turtle

turtle.colormode(255)
a = turtle.Turtle()

a.penup()
a.backward(100)
a.left(90)
a.backward(100)
a.right(90)
a.pendown()

for k in range(0,255,10):
    a.pensize(k)
    a.color(0,k,k)
    a.forward(10)


a.penup()
for k in range(255,0,-10):
    a.backward(10)

a.left(90)
a.pendown()

for k in range (0,255,10):
    a.pensize(k)
    a.color(0,k,k)
    a.forward(10)