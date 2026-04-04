import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURE_NAMES = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education',
    'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement',
    'JobLevel', 'JobSatisfaction', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike',
    'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TotalWorkingYears',
    'TrainingTimesLastYear', 'WorkLifeBalance',
    'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

def load_and_preprocess(path):
    """
    Loads raw employee attrition data from a CSV file and preprocesses it.
    
    This function handles:
    - Encoding the binary target variable (Attrition).
    - Subsetting to only the explicitly supported numerical 23 features.
    - Scaling all numerical features using StandardScaler.
    
    Args:
        path (str): The file path to the CSV dataset.
        
    Returns:
        tuple: A 4-tuple containing X_scaled, y, scaler, feature_names.
    """
    df = pd.read_csv(path)

    # Encode the target variable into a binary format (1 for Attrition, 0 for Retention)
    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})
    y = df["Attrition"]

    # Keep only the features that the web app natively supports
    X = df[FEATURE_NAMES]

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns
