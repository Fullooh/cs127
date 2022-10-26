#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

#Import libraries.
import matplotlib as plt
import pandas as pd

#Read in the csv file.
lead = pd.read_csv('children_lead.csv')

choice = input("Enter a choice: a. group by borough b. group by year")



if choice == 'a':
    groupedData = lead.groupby('borough')
    #Group the data by borough
    i = (groupedData["affected_children"].mean())
    print("average number of affected children by borough")
    print(i)

    x = input("Enter a borough: ")
    aff = groupedData.get_group(x)

    print( "average number of affected children of", x , "is" , aff["affected_children"].mean())
    print( "min number of affected children of", x , "is" , aff["affected_children"].min())
    print( "max number of affected children of", x , "is" , aff["affected_children"].max())

elif choice == "b":

    aff = lead.groupby("year")
    print("average number of affected children my year")
    print(aff['affected_children'].mean())
    
    year = int(input('Enter a year(2005 - 2016): '))
    year_group = aff.get_group(year)
    print("average number of affected children in", year, "is" , year_group["affected_children"].mean())
    print("min number of affected children in", year, "is" , year_group["affected_children"].min())
    print("max number of affected children in", year, "is" , year_group["affected_children"].max())

else:
    print("wrong choice")
