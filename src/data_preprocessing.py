import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Drop employee identifier
    if "EmployeeNumber" in df.columns:
        df.drop("EmployeeNumber", axis=1, inplace=True)

    # Encode target
    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

    # Encode categorical features
    categorical_cols = df.select_dtypes(include="object").columns
    for col in categorical_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop("Attrition", axis=1)
    y = df["Attrition"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns
