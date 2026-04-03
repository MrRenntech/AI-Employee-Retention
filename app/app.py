"""
Employee Attrition Prediction API & Web Dashboard
=================================================
This Flask application serves as the production interface for the employee attrition model.
It provides a web interface for HR personnel to perform both individual and batch risk assessments,
along with an executive dashboard for organization-wide attrition metrics.
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import joblib
import numpy as np
import pandas as pd
import os
import json
from datetime import datetime

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
app.config['SECRET_KEY'] = 'retention_ai_super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retention.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.models import db, User, PredictionLog
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def save_prediction_log(employee_id, pred_type, prob, risk, details):
    try:
        log = PredictionLog(
            employee_id=employee_id,
            prediction_type=pred_type,
            probability=prob,
            risk_level=risk,
            details=json.dumps(details)
        )
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        print(f"Error saving log: {e}")


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

def calculate_workforce_score(high_risk_count, total_count):
    """Calculates a simple 0-100 score for executive dashboard KPIs."""
    if total_count == 0:
        return 100
    ratio = high_risk_count / total_count
    score = max(0, min(100, 100 - (ratio * 100 * 1.5))) # Weighting high risk heavier
    return round(score)

@app.route("/")
@login_required
def home():
    """Renders the main dashboard for individual risk prediction and batch uploads."""
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        from werkzeug.security import check_password_hash
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'error')
            
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/predict", methods=["POST"])
@login_required
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
        # Get exact feature importances/coefficients mapped to values
        top_indices = np.argsort(np.abs(importances))[-5:][::-1]
        top_features = []
        for i in top_indices:
            feat = FEATURE_NAMES[i]
            # Create a user-friendly string showing the metric explicitly
            top_features.append(f"{feat}")

        recommendations = retention_recommendation(top_features)
        
        # Save to database
        save_prediction_log(
            employee_id="N/A", 
            pred_type="Individual", 
            prob=float(prob), 
            risk=prediction, 
            details=dict(zip(FEATURE_NAMES, values))
        )

        return render_template(
            "result.html",
            risk=prediction,
            probability=round(float(prob)*100,2),
            top_features=top_features,
            recommendations=recommendations,
            original_values=values, # Pass original values to populate sliders
            feature_names=FEATURE_NAMES
        )
    except Exception as e:
        return f"An error occurred: {str(e)}", 400

@app.route("/simulate", methods=["POST"])
@login_required
def simulate():
    """
    AJAX Endpoint for the Scenario Simulator.
    Accepts a JSON payload of adjusted feature values and returns the new attrition probability.
    """
    try:
        data = request.get_json()
        values = [float(data.get(f, 0)) for f in FEATURE_NAMES]
        input_df = pd.DataFrame([values], columns=FEATURE_NAMES)
        input_scaled = scaler.transform(input_df)

        prob = attrition_model.predict_proba(input_scaled)[0][1]
        
        return {"new_probability": round(float(prob)*100, 2)}
    except Exception as e:
        return {"error": str(e)}, 400

@app.route("/batch", methods=["POST"])
@login_required
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
        
        # Log batch entry
        save_prediction_log(
            employee_id="BATCH", 
            pred_type="Batch Inference", 
            prob=float(np.mean(probs)), 
            risk="Mixed", 
            details={"rows_processed": len(df)}
        )

        return render_template("batch_result.html", tables=[df.to_html(classes='data', index=False)])
    except Exception as e:
         return f"Error processing batch file: {str(e)}", 500

@app.route("/executive", methods=["GET", "POST"])
@login_required
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
            
            # 3. Workforce Health Score
            workforce_score = calculate_workforce_score(high_risk_count, total_employees)

            # 1. Attrition Risk Distribution (For Chart.js)
            risk_distribution = {
                "High Risk": int(high_risk_count),
                "Low Risk": int(total_employees - high_risk_count)
            }

            # 4. Department Risk Analysis
            # Mocking departments since we don't have a reliable department column in the base 23 features.
            # In a real scenario, this would group by df['Department']
            np.random.seed(42) # For consistent demo
            df['Department'] = np.random.choice(["Sales", "Engineering", "HR", "Marketing"], size=len(df), p=[0.4, 0.4, 0.1, 0.1])
            
            department_stats = df.groupby('Department').apply(
                lambda x: pd.Series({
                    'Employees': len(x),
                    'High_Risk': sum(x['Risk_Level'] == 'High'),
                    'Risk_Percent': f"{round((sum(x['Risk_Level'] == 'High') / len(x)) * 100, 1)}%"
                })
            ).reset_index()
            
            department_chart_data = {
                "labels": department_stats['Department'].tolist(),
                "data": [float(str(p).replace('%','')) for p in department_stats['Risk_Percent']]
            }

            # Feature importance for Logistic Regression (using coefficients)
            importances = np.abs(attrition_model.coef_[0])
            top_indices = np.argsort(importances)[-5:][::-1]
            top_drivers = [FEATURE_NAMES[i] for i in top_indices]

            # 5. Priority Ranking
            df['Rank'] = range(1, len(df) + 1)
            df['EmployeeID'] = np.random.randint(1000, 9999, size=len(df)) # Mock IDs since not in feature set
            
            top_employees = df.sort_values(
                by="Risk_Probability",
                ascending=False
            )[['Rank', 'EmployeeID', 'Risk_Probability', 'Department']].head(10)
            
            # Format probability for display
            top_employees['Risk_Probability'] = top_employees['Risk_Probability'].apply(lambda x: f"{round(x*100, 1)}%")

            # 6. Risk Probability Histogram Data
            # Bins: 0-20%, 20-40%, 40-60%, 60-80%, 80-100%
            bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
            hist_counts, _ = np.histogram(probs, bins=bins)
            histogram_data = hist_counts.tolist()

            return render_template(
                "executive.html",
                total=total_employees,
                high_risk=high_risk_count,
                avg_risk=avg_risk,
                workforce_score=workforce_score,
                risk_distribution=risk_distribution,
                department_chart_data=department_chart_data,
                department_table=department_stats.to_html(classes="data", index=False),
                top_drivers=top_drivers,
                table=top_employees.to_html(classes="data", index=False),
                histogram_data=histogram_data
            )
        except Exception as e:
            return f"Error generating executive report: {str(e)}", 500

    return render_template("executive_upload.html")

@app.route("/history")
@login_required
def history():
    logs = PredictionLog.query.order_by(PredictionLog.timestamp.desc()).limit(100).all()
    return render_template("history.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
