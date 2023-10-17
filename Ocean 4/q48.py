
def writeNaturalNumber(n):
    file = open("output.txt", 'w')

    for i in range(n+1):
        file.write(str(i))
        file.write('\n')

n = int(input("Enter the number : "))
writeNaturalNumber(n)
