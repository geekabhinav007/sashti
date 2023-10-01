# 3. Print the following using four print statements:

# *
# **
# ***
# ****

n = int(input("Enter number of row of traiangle you want to print : "))

for i in range(1, n+1):
    for j in range(0, i):
        print("*", end=" ")
    print()
