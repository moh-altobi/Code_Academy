inputOK= False

while (inputOK== False):
    try:
        num = input("Enter a number: ")
        num = float(num)
        inputOK = True
    except ValueError:
        print("Non-numeric type entered '%s'"%num)

num = num * 2
print(num)