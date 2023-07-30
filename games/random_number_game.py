import random
a= ""
x=random.randint(0,100)

while(a != "done"):
    
    print("what is the number: ")
    a=int(input())
    if (a==x):
        print("you are right")
        a="done"
    elif (a > x):
        print("go leas than that")
    elif (a < x):
        print("go higher")
    else:
        print("you are wrong")


