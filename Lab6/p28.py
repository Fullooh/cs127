#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

#Import libraries.
import pandas as pd

#Read in the csv file.
rain = pd.read_csv('AustraliaRain.csv')

#Group the data by location
groupedData = rain.groupby('Location')

#Print the average rainfall
print(groupedData['Rainfall'].mean())

