# 33. Write a function called add that takes two numbers as arguments and returns their sum. (1 point)

def sum(a, b):
    return a + b


a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))

print("Sum of", a, "and", b, "is", sum(a, b))
