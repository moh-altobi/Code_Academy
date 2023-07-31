def total(*args): #unpacking
    sum=0
    for i in args:
        sum += i
    print(args)  #args is a tuple
    return sum


print(total(1,2,3,3,3)) #prints (1, 2, 3)

