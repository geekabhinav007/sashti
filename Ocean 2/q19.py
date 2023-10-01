# 19. Print Star Pattern: Write a program that takes a number n from the user and prints a right-angled triangle pattern with stars of n rows (1 point) .
n = int(input("Enter the no of rows : "))

for i in range(2, n+2):
    for j in range(1,i):
        print("*" , end = " ")
    print()

