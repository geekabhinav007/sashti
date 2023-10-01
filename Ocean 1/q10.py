# 10. Write a program to find out if the given number is prime or not (1 point).


n = int(input("Enter the number : "))
flag = 1
for i in range(2, n):
    if (n % i == 0):
        flag = 0
        print(n, "is a non-prime number.")
        break
if (flag == 1):
    print(n, "is a prime number.")
