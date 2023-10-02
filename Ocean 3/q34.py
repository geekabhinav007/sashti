# 34. Write a function called factorial that takes an integer n and returns the factorial of n. (1 point)

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


n = int(input("Enter the number n : "))

print("Factorial of number", n, "is", factorial(n))
