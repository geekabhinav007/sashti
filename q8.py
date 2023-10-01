# 8. Write a program that calculates and prints the sum of all numbers from 1 to n, where n is provided by the user (1 point).

num = int(input("Enter the number n: "))
sum = 0
for i in range(num+1):
    sum = sum + i
print(sum)
