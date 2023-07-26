unit = int(input("enter unit of electricity: "))


if unit < 100:
    print("no charge your bill=",unit)
elif 200>=unit >= 100:
    print("your bill=",unit*0.024)
elif unit > 200:
    print("your bill=",unit*0.047)    
else:
    print("invlid unit")

