# 9. Write a program that takes a number n from the user and prints the multiplication table for that number from 1 to 10. Generalize it from i to j
n = int(input("Enter the number : "))
i = 1
j = 10
for i in range(i, j+1):
    print(n, " X ", i, " = ", n*i)
