SIM = input("please enter phone nember with (+968) and 8 number: ")
length= len(SIM)

if length == 12 and SIM[0]=="+" and SIM[1:4]=="968" and SIM[4:].isdigit():
    print ("the number is valid")
else:
    print ("the number is not valid")

