dec={1:{"name":"jone","age":26,"sex":"male"},
     2:{"name":"marie","age":22,"sex":"female"},
     3:{"name":"sali","age":23,"sex":"female"}}

for i in dec:
    if dec[i]["age"] > 22 :
        print(dec[i]["name"],dec[i]["age"])
   

