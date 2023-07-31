import random
def random_number_game():
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

def sum_random_number_game():
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

a=int(input("enter 1 for random number game\nenter 2 for sum random number game\n"))
if (a==1):
    random_number_game()
elif (a==2):
    sum_random_number_game()