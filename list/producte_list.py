sum=1
sum1=0
mylist=[3,-5,-1,-7,2,8]
for i in range (len(mylist)):
    print(mylist[i],end=" * ")
#     print ("place in list",i,"number in list",mylist[i])
    sum*=mylist[i]
    if mylist[i]<0:
        sum1+=1
print ("=",sum,"\n",sum1,"elements in list are negative")