import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

departments = ["Sales", "Research & Development", "Human Resources"]
roles = ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"]
business_travels = ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
edu_fields = ["Life Sciences", "Other", "Medical", "Marketing", "Technical Degree", "Human Resources"]
genders = ["Male", "Female"]
marital_statuses = ["Single", "Married", "Divorced"]
overtimes = ["Yes", "No"]

data = []

for i in range(n):

    age = np.random.randint(22, 60)
    income = np.random.randint(3000, 20000)
    work_life = np.random.randint(1, 5)
    satisfaction = np.random.randint(1, 5)
    promotion_gap = np.random.randint(0, 10)

    # Simulate realistic risk behavior
    risk_factor = (
        (20000 - income) * 0.00005 +
        (5 - work_life) * 0.2 +
        (5 - satisfaction) * 0.2 +
        promotion_gap * 0.05
    )

    data.append({
        "Age": age,
        "BusinessTravel": np.random.choice(business_travels),
        "DailyRate": np.random.randint(100, 1500),
        "Department": np.random.choice(departments),
        "DistanceFromHome": np.random.randint(1, 30),
        "Education": np.random.randint(1, 5),
        "EducationField": np.random.choice(edu_fields),
        "EmployeeCount": 1,
        "EmployeeNumber": np.random.randint(1, 2000),
        "EnvironmentSatisfaction": satisfaction,
        "Gender": np.random.choice(genders),
        "HourlyRate": np.random.randint(30, 100),
        "JobInvolvement": np.random.randint(1, 5),
        "JobLevel": np.random.randint(1, 5),
        "JobRole": np.random.choice(roles),
        "JobSatisfaction": satisfaction,
        "MaritalStatus": np.random.choice(marital_statuses),
        "MonthlyIncome": income,
        "MonthlyRate": np.random.randint(10000, 30000),
        "NumCompaniesWorked": np.random.randint(0, 10),
        "Over18": "Y",
        "OverTime": np.random.choice(overtimes),
        "PercentSalaryHike": np.random.randint(10, 25),
        "PerformanceRating": np.random.randint(1, 5),
        "RelationshipSatisfaction": np.random.randint(1, 5),
        "StandardHours": 80,
        "StockOptionLevel": np.random.randint(0, 3),
        "TotalWorkingYears": np.random.randint(1, 35),
        "TrainingTimesLastYear": np.random.randint(0, 6),
        "WorkLifeBalance": work_life,
        "YearsAtCompany": np.random.randint(0, 20),
        "YearsInCurrentRole": np.random.randint(0, 10),
        "YearsSinceLastPromotion": promotion_gap,
        "YearsWithCurrManager": np.random.randint(0, 10)
    })

df = pd.DataFrame(data)

df.to_csv("data/ai_based_dataset.csv", index=False)

print("Realistic demo dataset created")
