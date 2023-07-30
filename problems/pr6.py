n = int (input ("enter the length of list grater then 5,and less then 100000: "))
if 5<n<= (10**5):
    my_list=[]
    print("enter",n ,"elements for the list:")
    for i in range(n):
        val = int(input())
        my_list.append(val)
    print(my_list)
cout = 0
c =''
x = []
for i in my_list:
    cout = 0
    for j in range(len(my_list)):
      if i == my_list[j]:
          cout +=1
          if cout >= 3 and i not in x: #greater than 3 times
                x.append(i)
          
print(x)
