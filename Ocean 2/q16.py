# 16. Write a program that counts and prints the number of vowels and the number of consonants in the string (1 point).

str = input("Enter the string: ")
countv = 0
countc = 0
for char in str:
    if (char in "aieouAEIOU"):
        countv = countv + 1
    else:
        countc = countc + 1
print("consonants is ", countc)
print("vowels is ", countv)
