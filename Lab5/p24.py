#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

List = input("Enter a list of words, seperated by a space: ")

word = List.split()

count = 0

for i in word:
    if i[-1] == "a" or i[-1] == "b":
        count += 1


print("Number of words:", len(word))

print("Number of words ending with a or b:" , count)

print("Fraction of your words ending in a or b:", count/len(word))
