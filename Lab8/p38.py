#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import turtle
import math

def drawPantegon(t, length, numEdges):
   if numEdges > 0:
        t.forward(length)
        t.left(72)
        drawPantegon(t,length,numEdges-1)

def cornerPantegon(t, length):
    if length >= 25:
        drawPantegon(t, length, 5)
        length = length//2
        cornerPantegon(t,length)

def nestedPantegon(t, length):
    if length >= 25:
        drawPantegon(t,length,5)
        t.forward(length/2)
        t.left(36)
        pos = t.position()
        nestedPantegon(t,length*math.sin(54/180*math.pi))