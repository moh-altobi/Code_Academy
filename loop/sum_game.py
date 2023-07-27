import random
a= ""
while(a != "done"):
    x=random.randint(0,100)
    y=random.randint(0,100)
    print("what is the sum of" ,x,"+",y,"=",)
    right_sum = str (x+y)
    a=input()
    if (a==right_sum):
        print("you are right")
    elif (a=="done"):
        print("well done")
    else:
        print("you are wrong")


