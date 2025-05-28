def Drug_dosage_calculator(weight, age):
# Function to calculate drug dosage based on weight and age
    if weight <= 0 or age <= 0:# Check if weight and age are positive numbers
        print("Weight, age, and dosage must be positive numbers.")
        return None
    if age > 18:# Check if the patient is an adult
        print("Sorry,this system is not suit for Adult patient")
        return None
    else :# If the patient is a child, calculate the dosage
        mg = weight *15
        dosage = mg / 120 * 5
        print(f"The dosage of the drug is {dosage} ml")
        return None
weight = float(input("Enter the weight of the patient in kg: "))
age = int(input("Enter the age of the patient in years: "))

Drug_dosage_calculator(weight, age)

