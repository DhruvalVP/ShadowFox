"""
Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"

"""
# ----- input Height and Weight ----- #
height = float(input("Enter Height in Meters: "))
weight = float(input("Enter Weight in Kilograms: "))

# ----- Calculate BMI ----- #
BMI = weight/(height*height)

# ----- Condition on BMI ----- #
if BMI>=30:
    print("Obesity")

elif BMI>=25 and BMI<=29:
    print("Overweight")

elif BMI>=18.5 and BMI<=25:
    print("Normal")

elif BMI<18.5:
    print("Underweight")

# ----- Exit Program ----- #
exit()