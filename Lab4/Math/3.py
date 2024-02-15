import math
n = int(input())
a = int(input())
print("Input number of sides: ", n)
print("Input the length of a side: ", a)
area = ((a**2) * n) / (4 * math.tan(math.pi/n))
print("The area of the polygon is: ", area)