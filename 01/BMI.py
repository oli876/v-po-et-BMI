weight = int(input("Enter the weight: "))
height = float(input("Enter the height: "))

result = weight / height ** 2

if result < 18.5:
    print("Underweight")
elif result >= 18.5 and result <= 25:
    print("Normal")
elif result >= 25 and result <= 30:
    print("Overweight")
else:
    print("Obesity")
