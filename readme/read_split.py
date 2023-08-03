input_file= open("split.txt","r")

for line in input_file:
    line=line.rsplit()
    
    print(line)