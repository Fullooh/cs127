#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

binaryNum = ""

binaryNum = input("Enter a string with 0 or 1 only: ")

num = 0

base = 2

weight = 1

length = len(binaryNum)

ch = " "

for i in binaryNum[::-1]:
        ch = i
        if ch == "1":
            num += weight
        elif ch!= "0":
            print("Letter", ch, "is not allowed in binary string.")
            exit()
        weight *= base

print(str(num))
