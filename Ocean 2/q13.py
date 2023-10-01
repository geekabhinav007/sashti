# 13. Take two strings of the same length and intersperse the second one into the first one:

str1 = input("Enter first String : ")
str2 = input("Enter two String : ")


n = len(str1)

m = len(str2)
l = 0
i = 0
j = 0
while (True):
    if (l % 2 == 0):
        print(str1[i], end="")
        i = i + 1
        l = l + 1
    else:
        print(str2[j], end="")
        j = j + 1
        l = l + 1
    if(i >= n and j >= m):
        print()
        break
