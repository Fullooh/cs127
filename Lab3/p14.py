#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import numpy as np
import matplotlib.pyplot as plt

inFile=input("Enter name of the input file: ")

img = plt.imread(inFile)
img[:,:,0]=0

outFile=input("Enter name of the output file: ")
plt.imsave(outFile,img)