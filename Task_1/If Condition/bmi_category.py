height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
BMI = weight / (height ** 2)
print(BMI)

if BMI >= 30:
    print("Obesity")
elif BMI >= 25 and BMI <= 29:
    print("Overweight")  
elif BMI >= 18.5 and BMI <25:
    print("Normal")
else:
    print("Underweight")         