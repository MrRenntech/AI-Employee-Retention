import pandas as pd
import numpy as np
import os

np.random.seed(42)

# Using 2000 employees for a robust test of the dashboard components
num_employees = 2000

data = {
    "Age": np.random.randint(21, 60, num_employees),
    "DailyRate": np.random.randint(100, 1500, num_employees),
    "DistanceFromHome": np.random.randint(1, 30, num_employees),
    "Education": np.random.randint(1, 5, num_employees),
    "EnvironmentSatisfaction": np.random.randint(1, 5, num_employees),
    "HourlyRate": np.random.randint(30, 100, num_employees),
    "JobInvolvement": np.random.randint(1, 5, num_employees),
    "JobLevel": np.random.randint(1, 5, num_employees),
    "JobSatisfaction": np.random.randint(1, 5, num_employees),
    "MonthlyIncome": np.random.randint(2000, 20000, num_employees),
    "MonthlyRate": np.random.randint(10000, 30000, num_employees),
    "NumCompaniesWorked": np.random.randint(0, 10, num_employees),
    "PercentSalaryHike": np.random.randint(10, 25, num_employees),
    "PerformanceRating": np.random.randint(1, 5, num_employees),
    "RelationshipSatisfaction": np.random.randint(1, 5, num_employees),
    "StockOptionLevel": np.random.randint(0, 3, num_employees),
    "TotalWorkingYears": np.random.randint(1, 35, num_employees),
    "TrainingTimesLastYear": np.random.randint(0, 6, num_employees),
    "WorkLifeBalance": np.random.randint(1, 5, num_employees),
    "YearsAtCompany": np.random.randint(0, 20, num_employees),
    "YearsInCurrentRole": np.random.randint(0, 10, num_employees),
    "YearsSinceLastPromotion": np.random.randint(0, 10, num_employees),
    "YearsWithCurrManager": np.random.randint(0, 10, num_employees)
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)
df.to_csv("data/fake_employee_dataset.csv", index=False)

print(f"Fake dataset generated: data/fake_employee_dataset.csv with {num_employees} employees")
