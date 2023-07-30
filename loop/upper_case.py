massege = input("please enter the massege :")

uppercase = 0
for char in massege:
    if char.isupper():
        uppercase = uppercase + 1

print(uppercase)