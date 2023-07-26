state = input("Are you graduat Enter Y or N : ")
age = int(input("enter your age: "))


if age >= 18:
    if state =="Y":
        print("graduated and",age,"years old")
    else:
        print("not graduated and",age,"years old")  
else:
    print("under 18 years old")