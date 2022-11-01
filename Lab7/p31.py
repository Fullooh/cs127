#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

import matplotlib.pyplot as plt
import pandas as pd

internet = pd.read_csv("country_internet.csv")

output = input("Enter output file name: ")

internet["Percentage"] = (internet["Internet users"]/internet["Population"]) * 100

internet.plot(x = "Country", y = "Percentage")

max_id = internet["Percentage"].idxmax()

print("Maximum percentage of all countries:", internet["Country"][max_id], round(internet["Percentage"].max(),2)), "%"

fig = plt.gcf()
fig.savefig(output)

