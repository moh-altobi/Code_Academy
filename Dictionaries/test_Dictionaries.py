contact={"Fred":7235591,
         "Mary":3841212,
         "Bob":3841122,
         "Sarah":7459658}

oldcontact=dict(contact)
print(contact["Fred"])

if "Bob" in contact:
    print(contact["Bob"])
else:
    print("Jone is not in my contact")

number= contact.get("c",411) #like if statmint
print("Dial",str(number))


contact["mulham"]=4545251
print(contact)

contact["Bob"]=9568652
print(contact)

removenumber=contact.pop("Bob")

print(contact)
print(removenumber)

for key in contact:
    print(key,contact[key])
print("--"*15)
for item in contact.items():
    print(item[0],item[1])