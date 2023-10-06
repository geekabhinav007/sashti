n = int(input("Enter the size of square matrix : "))
A_Matrix = []
for i in range(n):
    print("Enter the", i+1, "Row of Matrix  of" , n , "X" ,n ,  ": ")
    row = input()
    ele = [int(x) for x in row.split()]
    A_Matrix.append(ele)

B_Matrix = []
for i in range(n):
    print("Enter the", i+1, "Row of Matrix  of" , n , "X" ,n ,  ": ")
    row = input()
    ele = [int(x) for x in row.split()]
    B_Matrix.append(ele)

print("The Matrix A is :")
for i in range(n):
    print(A_Matrix[i])

print("The Matrix B is :")
for i in range(n):
    print(B_Matrix[i])

ans = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(A_Matrix[i][j] + B_Matrix[i][j])
    ans.append(row)


print("Sum of Two Matrix is : ")
for row in ans:
    print(row)
        

