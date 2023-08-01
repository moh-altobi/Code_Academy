list1=[10,20,30,90]
limit=90
pos=0
found= False

while pos < len (list1) and not found:
    if list1 [pos]==90:
        found=True
    else:
        pos=pos+1
    
if found:
    print("the number 90 found in position: ",pos)
else:
    print("not found")
