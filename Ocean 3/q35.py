# 35. Write a function called fibonacci that takes an integer n and returns the n-th number in the Fibonacci sequence. (1 point)


def fib(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n = int(input("Enter the number n : "))

print("The", n , "th term number in the Fibonacci sequence is" , fib(n))