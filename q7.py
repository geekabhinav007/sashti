# 7. Print a sequence of numbers starting from the number a with common difference d. Go on till you reach the number b.

start = int(input("Enter the value of start : "))
common_difference = int(input("Enter the value of common difference : "))

end = int(input("Enter the value of End : "))

for i in range(start, end, common_difference):
    print(i, end=" ")
