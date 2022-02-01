sq = int(input("Enter the side of a square:"))
print("Area of square:",(lambda x:x**2)(sq))

l = int(input("Enter the length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
print("Area of rectangle:",(lambda x,y:x*y)(l,b))

h = int(input("Enter the height of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
print("Area of triangle:",(lambda x,y:0.5*x*y)(b,h))