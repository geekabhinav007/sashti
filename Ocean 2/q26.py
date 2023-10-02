# 26. Divisible by 7 and 5: Write a program that checks if a number provided by the user is divisible by both 7 and 5. Generalize it to a and b (1 point).
num = int(input("Enter Number : "))

a = 7
b = 5

if (num % a == 0 and num % b == 0):
    print(num, "is divisble by both", a, b)
else:
    print(num, "is not divisble by both", a, "and", b)
