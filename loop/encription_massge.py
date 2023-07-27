text=input("pleas enter the massge: ")
for letter in text:
    ascii = int (ord(letter)-3) #encripeted massge from khoor to hello
    print(chr(ascii),end="")