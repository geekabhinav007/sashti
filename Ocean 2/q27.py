# 27. Create a Python program that prompts the user for their age. If the age is less than 18, print “You are a minor.” If the age is between 18 and 65, print “You are an adult.” Otherwise, print “You are a senior citizen.” (1 point).


age = int(input("Enter the age : "))

if (age < 18 and age > 0):
    print("You are a minor.")
elif (age >= 18 and age < 65):
    print("You are an Adult")
elif (age >= 65 and age <=100):
    print("You are a senior citizen.")
else:
    print("Invalid age")
