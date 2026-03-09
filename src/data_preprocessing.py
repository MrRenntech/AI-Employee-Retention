import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path):
    """
    Loads raw employee attrition data from a CSV file and preprocesses it.
    
    This function handles:
    - Removing unnecessary identifier columns.
    - Encoding the binary target variable (Attrition).
    - Encoding all categorical features using LabelEncoder.
    - Scaling all numerical features using StandardScaler.
    
    Args:
        path (str): The file path to the CSV dataset.
        
    Returns:
        tuple: A 4-tuple containing:
            - X_scaled (numpy.ndarray): The preprocessed and scaled feature matrix.
            - y (pandas.Series): The encoded target variable.
            - scaler (StandardScaler): The fitted scaler object used for normalization.
            - feature_names (pandas.Index): The list of column names used in the feature matrix.
    """
    df = pd.read_csv(path)

    # Drop employee identifier as it has no predictive power
    if "EmployeeNumber" in df.columns:
        df.drop("EmployeeNumber", axis=1, inplace=True)

    # Encode the target variable into a binary format (1 for Attrition, 0 for Retention)
    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

    # Encode all categorical features using LabelEncoder
    categorical_cols = df.select_dtypes(include="object").columns
    for col in categorical_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    # Separate the features (X) from the target variable (y)
    X = df.drop("Attrition", axis=1)
    y = df["Attrition"]

    # Scale the features to ensure all variables have zero mean and unit variance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns
