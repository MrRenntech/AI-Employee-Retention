"""
Employee Attrition Prediction API & Web Dashboard
=================================================
This Flask application serves as the production interface for the employee attrition model.
It provides a web interface for HR personnel to perform both individual and batch risk assessments,
along with an executive dashboard for organization-wide attrition metrics.
"""
from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

# Define relative paths to models
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "attrition_model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "scaler.pkl")

# Load models safely
try:
    attrition_model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except FileNotFoundError:
    print(f"Error: Model files not found at {MODEL_PATH} or {SCALER_PATH}. Please run src/train_model.py first.")
    exit(1)

FEATURE_NAMES = [
    'Age','DailyRate','DistanceFromHome','Education',
    'EnvironmentSatisfaction','HourlyRate','JobInvolvement',
    'JobLevel','JobSatisfaction','MonthlyIncome',
    'MonthlyRate','NumCompaniesWorked','PercentSalaryHike',
    'PerformanceRating','RelationshipSatisfaction',
    'StockOptionLevel','TotalWorkingYears',
    'TrainingTimesLastYear','WorkLifeBalance',
    'YearsAtCompany','YearsInCurrentRole',
    'YearsSinceLastPromotion','YearsWithCurrManager'
]

app = Flask(__name__)

def retention_recommendation(top_factors):
    """
    Generates tailored retention strategies mapped to an employee's specific risk drivers.
    
    Args:
        top_factors (list): A list of the most influential features driving attrition risk.
        
    Returns:
        list: Actionable recommendations for HR to intervene.
    """
    actions = []
    if "MonthlyIncome" in top_factors:
        actions.append("Compensation review recommended. Ensure pay is competitive for role.")
    if "WorkLifeBalance" in top_factors:
        actions.append("Improve work-life balance initiatives. Offer flexible schedules.")
    if "YearsSinceLastPromotion" in top_factors:
        actions.append("Career growth discussion required. Identify paths for advancement.")
    if "JobSatisfaction" in top_factors:
        actions.append("Manager engagement session suggested. Conduct targeted 1-on-1s.")
    if "EnvironmentSatisfaction" in top_factors:
        actions.append("Workplace environment assessment needed.")
    if "RelationshipSatisfaction" in top_factors:
        actions.append("Team building and interpersonal conflict resolution.")
    if not actions:
        actions.append("Regular engagement and continuous performance monitoring.")
    return actions

@app.route("/")
def home():
    """Renders the main dashboard for individual risk prediction and batch uploads."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint for predicting attrition risk for a single employee based on form inputs.
    Extracts form fields, scales inputs, predicts probability, and calculates key risk drivers.
    """
    try:
        values = [float(request.form.get(f)) for f in FEATURE_NAMES]
        input_df = pd.DataFrame([values], columns=FEATURE_NAMES)
        input_scaled = scaler.transform(input_df)

        prob = attrition_model.predict_proba(input_scaled)[0][1]
        prediction = "High Risk" if prob >= 0.6 else "Low Risk"

        importances = attrition_model.coef_[0] # LogisticRegression specific
        # For general models like RandomForest, use feature_importances_
        # importances = attrition_model.feature_importances_ 
        
        # Get absolute importance for ranking influence
        top_indices = np.argsort(np.abs(importances))[-3:][::-1]
        top_features = [FEATURE_NAMES[i] for i in top_indices]

        recommendations = retention_recommendation(top_features)

        return render_template(
            "result.html",
            risk=prediction,
            probability=round(float(prob)*100,2),
            top_features=top_features,
            recommendations=recommendations
        )
    except Exception as e:
        return f"An error occurred: {str(e)}", 400

@app.route("/batch", methods=["POST"])
def batch():
    """
    Endpoint for uploading a CSV of multiple employees to perform bulk risk assessment.
    Returns a rendered HTML template containing a sorted pandas DataFrame of the high-risk employees.
    """
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == '':
        return "No selected file", 400
        
    try:
        df = pd.read_csv(file)
        
        # Validate columns
        missing_cols = [col for col in FEATURE_NAMES if col not in df.columns]
        if missing_cols:
            return f"Missing columns in CSV: {', '.join(missing_cols)}", 400

        df_scaled = scaler.transform(df[FEATURE_NAMES])

        probs = attrition_model.predict_proba(df_scaled)[:,1]
        df["Attrition_Risk_Probability"] = probs
        df["Risk_Level"] = ["High Risk" if p>=0.6 else "Low Risk" for p in probs]

        df = df.sort_values(by="Attrition_Risk_Probability", ascending=False)

        return render_template("batch_result.html", tables=[df.to_html(classes='data', index=False)])
    except Exception as e:
         return f"Error processing batch file: {str(e)}", 500

@app.route("/executive", methods=["GET", "POST"])
def executive():
    """
    Endpoint for the Executive Dashboard.
    GET: Displays the CSV upload dialogue.
    POST: Processes a corporate-wide dataset, generating high-level metrics and a priority list.
    """
    if request.method == "POST":
        try:
            if 'file' not in request.files:
                return "No file part", 400
            file = request.files["file"]
            if file.filename == '':
                return "No selected file", 400

            df = pd.read_csv(file)

            # Validate columns
            missing_cols = [col for col in FEATURE_NAMES if col not in df.columns]
            if missing_cols:
                return f"Missing columns in CSV: {', '.join(missing_cols)}", 400

            df_scaled = scaler.transform(df[FEATURE_NAMES])
            probs = attrition_model.predict_proba(df_scaled)[:,1]

            df["Risk_Probability"] = probs
            df["Risk_Level"] = ["High" if p>=0.6 else "Low" for p in probs]

            total_employees = len(df)
            high_risk_count = sum(df["Risk_Level"] == "High")
            avg_risk = round(float(np.mean(probs))*100,2)

            # Feature importance for Logistic Regression (using coefficients)
            importances = np.abs(attrition_model.coef_[0])
            top_indices = np.argsort(importances)[-5:][::-1]
            top_drivers = [FEATURE_NAMES[i] for i in top_indices]

            top_employees = df.sort_values(
                by="Risk_Probability",
                ascending=False
            ).head(10)

            return render_template(
                "executive.html",
                total=total_employees,
                high_risk=high_risk_count,
                avg_risk=avg_risk,
                top_drivers=top_drivers,
                table=top_employees.to_html(classes="data", index=False)
            )
        except Exception as e:
            return f"Error generating executive report: {str(e)}", 500

    return render_template("executive_upload.html")
    
if __name__ == "__main__":
    app.run(debug=True)
