#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

myString = input("Enter an all-small-letter string: ")

shift = int(input("Enter a non-negative int to shift: "))

word = ""
for m in myString:

    if ord(m) + 13 >= 127:
        word += chr(ord(m) - 26 + shift)

    else:
        word += chr(ord(m) + shift)



print("ciphered string: " + word)



