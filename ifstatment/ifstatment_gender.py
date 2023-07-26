gender = input("Enter your gender M or F : ")
age = int(input("enter your age: "))

if gender.upper() =="M":
    if 24<= age <= 30:
        print("you are pass and accepted for the job")
    else:
        print("you are not accepted for the job")  
elif gender.upper() =="F":
    print("you are female, not accepted for the job")
else:
    print("you are not accepted for the job")