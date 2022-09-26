#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

names = input('Enter a list of names, separated by semicolon: ')
nameList = names.split(';')

for i in range(len(nameList)):
    nameList[i] = nameList[i].split()

print(nameList)

for i in nameList:
    print((i[0])[0:1]+'. '+i[1])