# 17. List of Squares: Write a program that prints the square of numbers from 1 to n, where n is provided by the user (1 point).

n = int(input("Enter the number n : "))

for i in range(1 , n+1):
    print(i*i , end = " ")