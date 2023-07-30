from math import *

def square(l):
    area=l*l
    return area

def circal(r):
    area=pi*r**2
    return area

def rectangel(l,m):
    area=l*m
    return area

def cylindar(r,h):
    area=2*pi*r(h+r)
    return area

def tringal(l,h):
    area=l*h/2
    return area
a=""
while(a!= "Q"):
    a=input("enter 1 for square area\nenter 2 for circal area\nenter 3 for rectangel area\nenter 4 for cylindar area\nenter 5 for tringal area\nor (q) for quit\n")
    a = a.upper()
    if (a==1):
        l=int(input("enter the side of square: "))
        print(square(l))
    elif (a==2):
        l=int(input("enter the radies of circal: "))
        print(circal(r))
    elif (a==3):
        l=int(input("enter the first side of rectangel: "))
        m=int(input("enter the second side of rectangel: "))
        print(rectangel(l,m))
    elif (a==4):
        r=int(input("enter the radies of cylindar: "))
        h=int(input("enter the hight of cylindar: "))
        print(cylindar(r,h))
    elif (a==5):
        h=int(input("enter the hight of tringal: "))
        l=int(input("enter the lenght of tringal: "))
        print(tringal(l,h))
