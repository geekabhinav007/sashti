# 25. Leap Year or Not: Write a program that checks if a given year is a leap year or not. Google for the details on how to figure out if the given number is a leap year or not. It is more complicated than simply checking for a multiple of 4 (1 point).
year = int(input("Enter the Year : "))

if (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year.")
