import joblib
import pandas as pd
import numpy as np
from data_preprocessing import load_and_preprocess

def load_artifacts():
    model = joblib.load("models/rf_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

def suggest_interventions(employee_row, feature_names):
    """
    Simple rule-based intervention logic based on common attrition drivers.
    In a real system, this would use SHAP values for personalized explanations.
    """
    interventions = []

    # Check for OverTime (assuming it was encoded, but we need original context or know encoding)
    # Since we don't have the original encoder objects saved for all columns in this simple script,
    # we will rely on checking the values against the training means or specific known high-risk values
    # if we had the raw data.
    
    # For now, we will add generic interventions based on high probability
    interventions.append("Schedule 1-on-1 career development meeting.")
    interventions.append("Review compensation package relative to market.")
    
    return interventions

def analyze_retention_risk(data_path="data/employee_attrition.csv", sample_size=5):
    X, y, scaler, feature_names = load_and_preprocess(data_path)
    model, _ = load_artifacts()

    # Predict probabilities
    probs = model.predict_proba(X)
    
    # Create a DataFrame with results
    results = pd.DataFrame(X, columns=feature_names)
    results['Attrition_Probability'] = probs[:, 1]
    results['Actual_Attrition'] = y.values

    # Filter for high risk employees
    high_risk = results[results['Attrition_Probability'] > 0.7]
    
    print(f"Total Employees Analyzed: {len(results)}")
    print(f"High Risk Employees Identified (>70%): {len(high_risk)}")
    
    print("\n--- Sample High Risk Cases & Interventions ---")
    for idx, row in high_risk.head(sample_size).iterrows():
        print(f"\nEmployee ID (Index): {idx}")
        print(f"Attrition Probability: {row['Attrition_Probability']:.2%}")
        
        actions = suggest_interventions(row, feature_names)
        print("Suggested Actions:")
        for action in actions:
            print(f"- {action}")

if __name__ == "__main__":
    analyze_retention_risk()
