#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import numpy as np
from matplotlib import pyplot as plt

filename=input('Enter output file name: ')

graph = np.empty([30,30,3])
graph[:,:,0]=1.0
graph[:,:,1]=1.0
graph[:,:,2]=0

for i in range(5,8,1):
    for j in range(5,25,1):
        graph[i,j,0]=0
        graph[i,j,1]=0
        graph[i,j,2]=1.0

for i in range(13,16,1):
    for j in range(8,25,1):
        graph[j,i,0]=0
        graph[j,i,1]=1.0
        graph[j,i,2]=0

#plt.imshow(graph)
#plt.show()

plt.imsave(filename,graph)
