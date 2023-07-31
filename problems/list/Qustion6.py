#Qustion6

sum1=0
mylist=[0,-5,-1,-7,0,8]
for i in range (len(mylist)):
    print(mylist[i],end=" , ")
    if mylist[i]==0:
        sum1+=1
print ("\n",sum1,"elements in list are zeros")