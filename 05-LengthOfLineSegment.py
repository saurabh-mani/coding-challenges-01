'''
Program Title: Length of Line Segment

Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
Examples

line_length([15, 7], [22, 11]) => 8.06

line_length([0, 0], [0, 0]) => 0

line_length([0, 0], [1, 1]) => 1.41

'''
import math

def line_length(dot1,dot2):
    return math.sqrt(((dot2[0]-dot1[0])**2)+((dot2[1]-dot1[1])**2))#Distance Formula: Distance = sqrt((x2-x1)^2+(y2-y1)^2)

x1 = float(input("Enter value for x1: "))
y1 = float(input("Enter value for y1: "))
x2 = float(input("Enter value for x2: "))
y2 = float(input("Enter value for y2: "))

dot1 = [x1,y1]
dot2 = [x2,y2]

print("Distance is "+str(round(line_length(dot1,dot2),2)))
