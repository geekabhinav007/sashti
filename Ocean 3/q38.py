# 38. Checking for Even or Odd: Write a function called is_even that takes an integer and returns True if the number is even, and False if it is odd. (1 point)

def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False


n = int(input("Enter the number n : "))

if (is_even(n)):
    print("Even Number")
else:
    print("Odd Number")
