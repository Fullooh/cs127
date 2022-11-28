#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----


import random

def player():
    num = int(input("Enter only 1-6: "))
    while num not in range(1,7):
        num = int(input("Input needs to be in 1-6. Re-enter: "))
    return num

def game():
    user = player()
    computer = random.randint(1,6)
    print(f"user: {user}")
    print(f"computer: {computer}")
    if user==computer:
        print("draw")
    else:
        if user+computer in [3,6,7,8]:
            print("user wins")
        else:
            print("computer wins")

def main():
    game()

if __name__ == '__main__':
    main()