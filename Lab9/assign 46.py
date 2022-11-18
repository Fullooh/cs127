#Name: Kevin Perez
#Email: KEVIN.PEREZ35@myhunter.cuny.edu

def isPerfect(num):
    total = 0
    if num <= 0:
        return False
    else:
        for i in range(1,(num//2)+1,1):
            if num%i == 0:
                total+=i
        return total == num
    

def main():
    num = int(input('Enter a perfect integer: '))
    while isPerfect(num) is False:
        print(f'{num} is not a perfect number.')
        num = int(input('enter another integer: '))
        isPerfect(num)
    print(f'Congratulations! {num} is a perfect number.')


if __name__ == '__main__':
    main()