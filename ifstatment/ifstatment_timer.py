time_h1 = int(input("enter the first time in hour from 1 to 24: "))
time_m1 = int(input("enter the first time in minits from 1 to 60: "))

time_h2 = int(input("enter the secand time in hour from 1 to 24: "))
time_m2 = int(input("enter the secand time in minits from 1 to 60: "))

print("first time is",time_h1,":",time_m1)
print("secand time is",time_h2,":",time_m2)



if time_h1 > time_h2:
    print("first time",time_h1,":",time_m1,"is after than","secand time",time_h2,":",time_m2)
elif time_h1 == time_h2:
    if time_m1 == time_m2:
        print("first time",time_h1,":",time_m1,"is =","secand time",time_h2,":",time_m2)
    elif time_m1 > time_m2:
        print("first time",time_h1,":",time_m1,"is after than","secand time",time_h2,":",time_m2)
    else:
        print("secand time",time_h2,":",time_m2,"is after than","first time",time_h1,":",time_m1)

else:
    print("secand time",time_h2,":",time_m2,"is after than","first time",time_h1,":",time_m1)

