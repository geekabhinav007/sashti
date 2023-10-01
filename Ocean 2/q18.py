# 18. Fibonacci Sequence : Write a program that prints the first n numbers in Fibonacci numbers (1 point).

def fib(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())

print(fib(n))