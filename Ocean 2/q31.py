'''
31. Write a program to populate a list L
 with the first n
 natural numbers (1 point).
'''
l = []
n = int(input("Enter the number n : "))

for i in range(1, n+1):
    l.append(i)
print(l)
