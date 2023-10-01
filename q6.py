# 6. Write a program to take as input a number n and display the first n natural numbers (1 point).

number = int(input("Enter the number n "))

for i in range(1, number+1):
    print(i, end=" ")
