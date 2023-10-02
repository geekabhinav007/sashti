# 39. Calculate Area of a Circle: Write a function called circle_area that takes the radius of a circle as an argument and returns its area. (1 point)
PI = 3.14


def Area(r):
    return PI*(r**2)


r = int(input("Enter the Radius : "))

print("Area of circle of radius", r , "is", Area(r))
