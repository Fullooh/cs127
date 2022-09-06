#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

word = input("Input: ")
newWord = ""

print("user reverse: ",word[::-1])

word = word.upper()

print("user reverse upper: ",word[::-1])

word = word.split()

for a in word:
    newWord = newWord + a[0]

print("user abbreviation: " + newWord)
