def Drug_dosage_calculator(weight, age):

    if weight <= 0 or age <= 0:
        print("Weight, age, and dosage must be positive numbers.")
        return None
    if age > 18:
        print("Sorry,this system is not suit for Adult patient")
        return None
    else :
        mg = weight *15
        dosage = mg / 120 * 5
        print(f"The dosage of the drug is {dosage} ml")
        return None
weight = float(input("Enter the weight of the patient in kg: "))
age = int(input("Enter the age of the patient in years: "))

Drug_dosage_calculator(weight, age)

