n=(input("pleas enter number"))
m=(len(n))
total=0
my_list=[]
while(int(n)>0):
    digit=int(n)%10
    
    print (int(digit),"^",m)
    x=digit**m
    print(x)
    total=total+digit
    n=(int(n)-digit)//10
    my_list.append(x)
#    if (n==x)
    print(my_list)

print ("the sum of the number",int(total),x)

    
