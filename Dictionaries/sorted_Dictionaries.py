dec={1:{"name":"jone","age":26,"sex":"male"},
     2:{"name":"marie","age":22,"sex":"female"},
     3:{"name":"sali","age":23,"sex":"female"}}

order= sorted(dec.items(), key=lambda x:x[1]["age"])

print(order)