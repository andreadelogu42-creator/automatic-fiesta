#-----------------------------------

# CALCULATOR BMI (Body Mass Index). 

#-----------------------------------
name = input("Name: ")
weight = int(input("Weight in (kg): "))
height = float(input("Height(in m, es 1.75): "))

bmi = weight / (height ** 2)
print(bmi)