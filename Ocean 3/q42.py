n = int(input("Enter the size of the list "))
num_list = list(int(num) for num in input(
    "Enter the list items separated by space ").strip().split())[:n]
max = num_list[0]
for item in num_list:
    if (item > max):
        max = item
print("Max  number in list is :", max)
