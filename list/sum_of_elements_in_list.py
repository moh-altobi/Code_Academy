sum=0
sum1=0
mylist=[3,5,1,7,2,8]
for i in range (len(mylist)):
    print(mylist[i],end="+")
#     print ("place in list",i,"number in list",mylist[i])
    sum+=mylist[i]
    
print ("=",sum)

for j in mylist:
    sum1+=j   
print (sum1)