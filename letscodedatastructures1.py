#radius of circle
import math
radius = float(input("Input the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area}")

#extension
filename = input("Input the Filename: ")
extension = filename.split(".")[-1]
print(f"The extension of the file is: '{extension}'")
