input_file= open("input.txt","r")
# line= input_file.readline()
for line in input_file:
    if int(line)%2==0:
        print(line)
