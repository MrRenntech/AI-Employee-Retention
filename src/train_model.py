"""
Model Training Pipeline
=======================
This script trains the baseline Logistic Regression model for employee attrition prediction.
It integrates with the data_preprocessing module, evaluates basic accuracy, and serializes
the resulting model and scaler artifacts for use in the Flask web application.
"""
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from data_preprocessing import load_and_preprocess

# 1. Load and preprocess the dataset
# This returns the scaled features, target variable, the fitted scaler, and the feature names.
X, y, scaler, feature_names = load_and_preprocess(
    "data/employee_attrition.csv"
)

# 2. Split the data into training and testing sets
# We use an 80/20 split and stratify based on the target variable to ensure proportional class representation.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Initialize and train the Logistic Regression baseline model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 4. Evaluate the model performance on the unseen test set
preds = model.predict(X_test)
print("Baseline Accuracy:", accuracy_score(y_test, preds))

# 5. Save the trained model and the scaler for deployment
joblib.dump(model, "models/attrition_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Baseline model saved successfully.")
