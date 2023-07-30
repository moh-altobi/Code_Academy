massege = input("please enter the massrgr: ")
sum=0
for i in massege:
    if i=="a" or i=="i" or i=="o" or i=="e" or i=="u":
        print(i,end=" ")
        sum+=1
print (sum)