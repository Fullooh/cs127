#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import numpy as np
from matplotlib import pyplot as plt

size = int(input("Enter the size: "))
output = input("Enter output file: ")

graph = np.empty([size,size,3])

graph[:,:,:]=0

for i in range(size):
    if i%2==0:
        graph[:,i,1]=0      #sets the green in every pixel in column i to 0
        graph[:,i,2]=1.0   #sets the blue in every pixel in column i to 255
    else:
        graph[:,i,1]=1.0
        graph[:,i,2]=0

plt.imsave(output,graph)