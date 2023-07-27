n=int(input("pleas enter number"))
total=0
while(n>0):
    digit=n%10
    
    print (int(digit))
    total=total+digit
    n=(n-digit)//10
print ("the sum of the number",int(total))

    