weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
age = float(input("Enter your age: "))

BMRM = (13.7516 * weight) + (5.0033 * height) - (6.755 * age) + 66.473
BMRW = (9.5634 * weight) + (1.8496 * height) - (4.6756 * age) + 66.473

print("Your BMRM is:", BMRM, ",", "while your BMRW is:", BMRW)
