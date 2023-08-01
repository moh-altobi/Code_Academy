def calculateAvergae(score):
    avreg=0
    for i in range (len(score)):
        avreg+=score[i]
    avreg=avreg/len(score)
    return avreg


values=[]
print("please enter sudent score, Q to quit")
userinput= input("")
while userinput.upper() !="Q":
    values.append(float(userinput))
    userinput=input("")
print(values)
print(calculateAvergae(values))
