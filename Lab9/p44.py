#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import turtle

def petal(color, angle):
    turtle.colormode(255)
    t = turtle.Turtle(visible=False)
    t.left(angle)
    for i in range(0,255,10):
        t.forward(10)
        t.pensize(i)
        if color == "red":
            t.pencolor(i,0,0)
        elif color == "green":
            t.pencolor(0,i,0)
        elif color == "blue":
            t.pencolor(0,0,i)
        elif color == "yellow":
            t.pencolor(i,i,0)
        elif color == "purple":
            t.pencolor(i,0,i)
        elif color == "cyan":
            t.pencolor(0,i,i)
        else:
            t.pencolor(0,i,0)

    

def flower(color,petals):
    angle = 0
    for i in range(petals):
        petal(color,angle)
        angle+=360/petals

def main():
    # color = 'green'
    # petals = '9'
    flower('green',9)
    turtle.done()

if __name__ == '__main__':
    main()
