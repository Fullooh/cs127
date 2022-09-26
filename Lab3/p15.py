#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

phrase = input('Enter a phrase: ')
words = phrase.split()

for i in range(len(words),0,-1):
    print(' '.join(words[:i]))
    
for i in range(len(words)-1):
    print(' '.join(words[:i+2]))
