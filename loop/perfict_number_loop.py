#perfict number the divided number of that and the sume of them are same
for i in range(1,101):
    cout = 0
    for j in range(1,i):
      if i%j ==0:
          cout +=j
    if i == cout:
        print(i)