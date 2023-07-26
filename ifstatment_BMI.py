weight = float(input("enter a weight in Kg: "))
height = float(input("enter a height in cm: "))

height=height/100

BMI=weight/(height**2)

if BMI < 18.5:
    print("your BMI=%.3f"%(BMI),"Underweight")
elif 25.0> BMI >= 18.5:
    print("your BMI=%.3f"%(BMI),"Normal")
elif 30.0> BMI >= 25.0:
    print("your BMI=%.3f"%(BMI),"Overweight")    
else:
    print("your BMI=%.3f"%(BMI),"Obese")