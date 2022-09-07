import turtle

turtle.colormode(255)
a = turtle.Turtle()
a.shape("turtle")
a.penup()
a.left(90)
a.pendown()
for k in range(0,255,10):
 a.forward(10)
 a.pensize(k)
 a.color(0,k,k)
a.penup()
for k in range(255,0,-10):
 a.backward(10)
a.pensize(0)
a.color(0,0,0)
a.right(90)
a.pendown()
for k in range (0,255,10):
 a.forward(10)
 a.pensize(k)
 a.color(0,k,k)
