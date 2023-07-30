SIM = input("please enter the card nember xxxx xxx: ")
length= len(SIM)

if length == 8 and SIM[0:4].isdigit() and SIM[4]==" " and SIM[5:].isdigit():
    print ("the number is valid")
else:
    print ("the number is not valid")


