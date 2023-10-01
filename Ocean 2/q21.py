# 21. Factorial: Write a program that calculates the factorial of a number provided by the user (1 point).

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)