from Graphics1 import Circle,Rectangle
from Graphics1.Graphics_3D import Cuboid,Sphere

r = float(input("Enter the radius of the circle:"))
Circle.area(r)
Circle.perimeter(r)

l = float(input("Enter the length of the rectangle:"))
b = float(input("Enter the breadth of the rectangle:"))
Rectangle.area(l,b)
Rectangle.perimeter(l,b)

h = float(input("Enter the height of the cuboid:"))
l = float(input("Enter the length of the cuboid:"))
b = float(input("Enter the breadth of the cuboid:"))

Cuboid.area(l,b,h)
Cuboid.volume(l,b,h)

r = float(input("Enter the radius of the sphere:"))

Sphere.area(r)
Sphere.volume(r)