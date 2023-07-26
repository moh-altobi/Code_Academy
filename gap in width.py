width=100
b=5
w=5
n=0

width=width-b

while width > 0 :
    width=width-w-b
    n=n+1
    if width < 0:
     break
width=width+w+b
print("the gap =",width/2)
print("number of tails",n*2-1)

 
#authrazed by mohammed altubi