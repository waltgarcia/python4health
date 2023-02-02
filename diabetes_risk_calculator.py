# Import necessary libraries
import numpy as np

# Define risk factors for diabetes
risk_factors = [
    "age >= 45 years",
    "overweight or obesity",
    "family history of diabetes",
    "physical inactivity",
    "history of gestational diabetes or polycystic ovary syndrome",
    "race/ethnicity (e.g., African American, Latino, Native American, Asian American, Pacific Islander)",
    "high-density lipoprotein cholesterol level < 35 mg/dL (0.90 mmol/L) and/or a triglyceride level > 250 mg/dL (2.82 mmol/L)",
    "hypertension (BP ≥ 140/90 mmHg or on therapy for hypertension)",
    "HDL cholesterol level < 35 mg/dL (0.90 mmol/L) and/or a triglyceride level > 250 mg/dL (2.82 mmol/L)",
    "impaired fasting glucose (IFG) on previous testing",
    "impaired glucose tolerance (IGT) on previous testing",
    "A1C ≥ 5.7% (39 mmol/mol)",
    "a physician-diagnosed of prediabetes"
]

# Define a function to calculate the risk score
def calculate_risk_score(risk_factors):
    # Assign a weight to each risk factor
    weight = np.array([1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2])
    score = 0
    
    # Loop through the risk factors and add the weight if the risk factor is present
    for i, factor in enumerate(risk_factors):
        if factor:
            score += weight[i]
    
    return score

# Define a function to determine the risk of diabetes based on the risk score
def determine_risk(score):
    if score < 8:
        return "Low Risk"
    elif score >= 8 and score <= 11:
        return "Moderate Risk"
    else:
        return "High Risk"

# Collect the risk factors from the user
patient_risk_factors = []
for factor in risk_factors:
    present = input(f"Is the patient affected by {factor}? (yes/no)")
    patient_risk_factors.append(present.lower() == "yes")

# Calculate the risk score
patient_score = calculate_risk_score(patient_risk_factors)

# Determine the risk of diabetes
risk = determine_risk(patient_score)

print(f"The patient is at {risk} of developing diabetes")