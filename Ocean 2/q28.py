# 28. Grading System: Write a program that takes the marks of five subjects from the user and calculates the grade according to the average marks: A if average >= 90 B if average >= 80 and < 90 C if average >= 70 and < 80 D if average >= 60 and < 70 F otherwise (1 point).

a, b, c, d, e = input.split()

avg = (int(a) + int(b) + int(c) + int(d) + int(e))/5

if (avg >= 90):
    print("A")
elif (avg < 90 and avg >= 80):
    print("B")
elif (avg < 80 and avg >= 70):
    print("C")
elif (avg < 70 and avg >= 60):
    print("D")
else:
    print("E")
