# 29. Decimal to Binary Conversion: Write a program that converts a decimal number to its binary representation using loops, without using built-in conversion functions (1 point).


n = int(input())

ans = ""

while (n != 1 ):
    ans = ans + str(n%2)
    n  = n//2
ans = ans+"1"

print(ans[::-1])

