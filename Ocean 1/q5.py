# Understand how to use a if conditional in python. Ask the user to enter a number and check if the number is even or odd (1 point).

number = int(input("Enter the number : "))

if(number % 2 == 0):
    print(number, " is Even." )
else:
    print(number, " is Odd." )