#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

myString = input("Enter a Message: ")

print("letter ASCII next_two_letter ")
for i in myString:
    print(i, ord(i), chr(ord(i) + 2))