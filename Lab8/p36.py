#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

def computePrice(liquid,sizeType):

  p=-1

  sizeType=sizeType

  if liquid=="coffee":

    if sizeType=="small":

      p=2.5

    elif sizeType=="medium":

      p=2.75

    #else:

    elif sizeType=="large":

      p=3.00

  elif liquid=="misto":

    if sizeType=="small":

      p=3.15

    elif sizeType=="medium":

      p=3.35

    #else: 

    elif sizeType=="large":

      p=3.7

  elif liquid=="mocha":

    if sizeType=="small":

      p=3.5

    elif sizeType=="medium":

      p=3.8

    elif sizeType=="large":

    #else: 

      p=4.25

  elif liquid=="tea":

    if sizeType=="small":

      p=2.35

    elif sizeType=="medium":

      p=2.45

    elif sizeType=="large":

    #else:

      p=2.90

  else:

    p=-1

  return float(p)