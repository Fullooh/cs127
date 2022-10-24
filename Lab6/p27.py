#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import matplotlib.pyplot as plt
import pandas as pd

file = input ("Enter a csv file: ")

borough = input("Enter a borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")

output = input ("Enter output name: ")

i = pd.read_csv(file)

print ("Min:", i[borough].min())

print ("Max: ", i[borough].max ())

print ("Mean: ", round(i[borough] .mean(),3))

print ("Median: ", i[borough].median())

print ("Median: ", round(i[borough].std(),3))

i['Fraction' ] = (i[borough]) / (i['case_count'])

i.plot(x = 'date_of_interest', y = 'Fraction')

fig = plt.gcf()
fig.savefig(output)