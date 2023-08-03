input_file= open("split.txt","r")

for line in input_file:
    data=line.rsplit()
    
    print(data[0])
    print(line[0])