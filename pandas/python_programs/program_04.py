import pandas as pd

patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Neha", "Rahul", "Priya", "Sneha"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "BP", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 20000, 75000, 10000, 55000]
}

df = pd.DataFrame(patients)
print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print("Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
