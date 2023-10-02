'''
32. Write a program to populate a list L
with random numbers in the range 1 to 1000 (1 point).
'''
import random

l = []

n = int(input("Enter the no of integers you want in a list : "))

for i in range(n):
    l.append(random.randint(1,1000))

print(l)