#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----


def flowerRecursion(t,n):
      if n > 0:
        t.forward(100)
        t.left(105) 
        t.forward(52) 
        t.left(105) 
        t.forward(100) 
        t.right(170)
        flowerRecursion(t,n - 1)