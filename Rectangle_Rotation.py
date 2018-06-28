"""
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example
For a = 6 and b = 4, the output should be 23

"""

def rectangle_rotation(a, b):
  a1 = filter(lambda x: x%2==0, [a//(2**0.5), a//(2**0.5)+1])[0]
  a2 = filter(lambda x: x%2==1, [a//(2**0.5), a//(2**0.5)+1])[0]
  b1 = filter(lambda x: x%2==0, [b//(2**0.5), b//(2**0.5)+1])[0]
  b2 = filter(lambda x: x%2==1, [b//(2**0.5), b//(2**0.5)+1])[0]
  return a1*b1+a2*b2
