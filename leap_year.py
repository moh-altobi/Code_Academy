years = int(input("plase enter your bearth year: "))


if years%400 == 0 or years%100 != 0 and years%4 == 0:
    print("this year is leap year")
else:
    print("this year is normal year")
