n = int (input ("enter the length of list grater then 5,and less then 100000: "))
if 5<n<= (10**5):
    my_list=[]
    print("enter",n ,"elements for the list:")
    for i in range(n):
        val = int(input())
        my_list.append(val)
    print(my_list)

    
else:
    print("invalid numbers")

