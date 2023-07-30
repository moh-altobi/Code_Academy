corect_anser="abcdabcd"
length=len(corect_anser)
mark=0
user_anser=input("plese enter the anser: ")

for i in range (length):
    if user_anser[i]==corect_anser[i] :
        mark+=1
        print(user_anser[i],end=" ")
    else:
        print("X", end=" ")
        
print("\nmark=",(mark/length)*100,"%")
