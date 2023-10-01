# 11. Write a program to take as input n and print all prime numbers upto and including n (1 point).


def checkPrime(n):
    flag = 1
    for i in range(2, n):
        if (n % i == 0):
            flag = 0
            return False
    if (flag == 1):
        return True


n = int(input("Enter the number : "))
for i in range(2, n+1):
    if (checkPrime(i)):
        print(i, end=" ")
