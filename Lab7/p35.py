#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

user = input("Enter hour (In 24hr time): ")

name = int(user)

if name < 12:
    print("Good Morning")
elif name < 17:
    print ("Good Afternoon")
else:
    print("Good Evening")
