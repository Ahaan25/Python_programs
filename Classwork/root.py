import cmath
import math
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
temp=(b**2)-(4*a*c)
root=(-b+cmath.sqrt(temp))/2*a
print(root)