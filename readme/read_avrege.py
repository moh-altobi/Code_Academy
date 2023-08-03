input_file= open("avrege.txt","r")
# line= input_file.readline()
sum1=0
avrege=0
i=0
for line in input_file:
    sum1=sum1+float(line)
    i+=1
avrege=sum1/i
print(avrege)
