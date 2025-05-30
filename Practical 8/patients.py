class patients:# Class to represent a patient record in a hospital
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    # Function to print patient record
    def print_record(self):
        print(f"Patient: {self.name}, Age: {self.age}, Last Admission: {self.admission_date}, History: {self.medical_history}")
# Function to update patient record
if __name__ == "__main__":
    patient1 = patients(
        name="Student X",
        age=19,
        admission_date="2025-4-8",
        medical_history="None"
    )
    print("Hospital Patient Records:")
    patient1.print_record()

    