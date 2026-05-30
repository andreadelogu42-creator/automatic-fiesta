#-----------------------------------

# CALCULATOR BMI (Body Mass Index). 

#-----------------------------------
name = input("Name: ").strip().tiitle()
weight = int(input("Weight in (kg): "))
height = float(input("Height(in m, es 1.75): "))
eta = int(input(Età: ")
                
# Calculation of BMI
bmi = weight / (height ** 2)

# Let's check the body mass index values

if bmi < 18.5:
    print("State: Underweight")
elif bmi < 25.0: 
    print("State: Normalweight")
elif bmi < 30.0: 
    print("State: Overeight")
else: 
    print("Obese")

print(f"{name} your BMI is: {bmi:.2f}")
