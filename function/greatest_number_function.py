def greatest(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
x=(int(input("plese enter first number: ")))
y=(int(input("plese enter second number: ")))
z=(int(input("plese enter therd number: ")))

print("the gretest nubmer is =",greatest(x,y,z))
