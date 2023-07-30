n=(input("pleas enter number"))
l=int(n)
m=(len(n))
total=0
my_list=[]
y=0
while(int(n)>0):
    digit=int(n)%10
    
    x=digit**m
    print(int(digit),"^",m,"=",x)
    total=total+digit
    n=(int(n)-digit)//10
    my_list.append(x)

for i in range(m):
    y+=int(my_list[i])
if (l==y):
    print ("The number is narcissists:",y)
else:
    print("The number is not narcissists")


    
