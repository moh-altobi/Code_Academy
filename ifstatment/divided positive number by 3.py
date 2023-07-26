number = int(input("enter the number: "))


if number > 0:
    if number%3 ==0:
        print("the number is divided by 3 and positive the is number =",number)
    else:
        print("the number is not divided by 3 and positive the number is =",number)
        print("the remanning of number by divided by 3 is =",number%3)

elif number == 0:
    print("the number is =",number)
else:
    print("the number is negative =",number)

