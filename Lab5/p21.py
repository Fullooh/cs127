#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import matplotlib.pyplot as plt
import numpy as np

filename=input('Enter file name: ')

t=float(input('Enter threshold: '))


ca = plt.imread('CaliforniaDrought_02232011_md.png')   

countSnow = 0                  

for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("number of white pixels:", countSnow)

print('percent of white pixels:', round(countSnow/16800,2),'%')

plt.imsave(filename, ca)



