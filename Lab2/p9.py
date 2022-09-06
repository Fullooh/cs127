#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: -----

myString = input("Enter an all-small-letter string: ")

shift = input("Enter a non-negative int to shift: ")

for m in myString:
    
 print(m, ord(m)+13, chr(ord(m) + 13))

 print("ciphered string: " + m)



