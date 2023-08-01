def multy(list1,multy):
    for i in range (len(list1)):
        list1[i]=list1[i]*multy
        return list1

values=[]
print("please enter value, Q to quit")
userinput= input("")
while userinput.upper() !="Q":
    values.append(float(userinput))
    userinput=input("")
print(values)
print(multy(values,5))
