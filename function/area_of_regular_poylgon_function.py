from math import *

def area_of_regular_poylgon(n,s):
    area=(n*s**2)/(4*tan(pi/n))
    return area
n=(float(input("plese enter the number side in regular polygon: ")))
s=(float(input("plese enter the side of regular polygon: ")))

print("the area of regular polygon is =",area_of_regular_poylgon(n,s))