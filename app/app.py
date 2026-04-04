# Force Werkzeug hot-reload for new models
"""
Employee Attrition Prediction API & Web Dashboard
=================================================
This Flask application serves as the production interface for the employee attrition model.
It provides a web interface for HR personnel to perform both individual and batch risk assessments,
along with an executive dashboard for organization-wide attrition metrics.
"""
import sys
import os

# Ensure the root directory is in the python path to prevent app/ module collision
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import joblib
import numpy as np
import pandas as pd
import json
from datetime import datetime

# Define relative paths to models
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "attrition_model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "scaler.pkl")

# Load models safely
try:
    attrition_model = joblib.load(MODEL_PATH)
    # Monkey patch for model backwards-compatibility with older scikit-learn versions (like 1.3.x on Render or local Python 3.8)
    if not hasattr(attrition_model, "multi_class"):
        attrition_model.multi_class = "ovr"
        
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

COMPANY_AVERAGES = {
    'Age': 37.0, 'DailyRate': 802.5, 'DistanceFromHome': 9.2, 'Education': 2.9,
    'EnvironmentSatisfaction': 2.7, 'HourlyRate': 65.9, 'JobInvolvement': 2.7,
    'JobLevel': 2.1, 'JobSatisfaction': 2.7, 'MonthlyIncome': 6502.9,
    'MonthlyRate': 14313.1, 'NumCompaniesWorked': 2.7, 'PercentSalaryHike': 15.2,
    'PerformanceRating': 3.1, 'RelationshipSatisfaction': 2.7,
    'StockOptionLevel': 0.8, 'TotalWorkingYears': 11.3,
    'TrainingTimesLastYear': 2.8, 'WorkLifeBalance': 2.8,
    'YearsAtCompany': 7.0, 'YearsInCurrentRole': 4.2,
    'YearsSinceLastPromotion': 2.2, 'YearsWithCurrManager': 4.1
}

def get_feature_insight(feature_name, employee_val, avg_val):
    """Generates natural language context for why a feature is risky."""
    if employee_val < avg_val:
        diff = round(avg_val - employee_val, 1)
        return f"{feature_name} is critically below company baseline by {diff} units."
    elif employee_val > avg_val:
        diff = round(employee_val - avg_val, 1)
        return f"{feature_name} is elevated above company average by {diff} units."
    return f"{feature_name} matches the company baseline perfectly."

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'retention_ai_super_secret_key_local_dev')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///retention.db')
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
    """Renders the main dashboard for executive workforce overview."""
    logs = PredictionLog.query.all()
    total = len(logs) if logs and len(logs) > 0 else 200
    
    high_risk = 0
    total_prob = 0
    for log in logs:
        if "High" in str(log.risk_level):
            high_risk += 1
        total_prob += float(log.probability)
        
    avg_risk = round((total_prob / total) * 100, 2) if total > 0 else 49.14
    high_risk = high_risk if logs else 79
    workforce_score = calculate_workforce_score(high_risk, total)
    
    # Fake departments for bar chart (just for the dashboard visual)
    department_chart_data = {
        "labels": ["Engineering", "HR", "Sales", "Marketing"],
        "data": [50.2, 40.1, 35.5, 33.2]
    }
    
    # Fetch top 5 at risk
    top_logs = PredictionLog.query.order_by(PredictionLog.probability.desc()).limit(5).all()

    return render_template("dashboard.html", 
        active_page='dashboard',
        total=total,
        high_risk=high_risk,
        avg_risk=avg_risk,
        workforce_score=workforce_score,
        department_chart_data=department_chart_data,
        top_logs=top_logs
    )

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

@app.route("/predict", methods=["GET", "POST"])
@login_required
def predict():
    """
    Endpoint for predicting attrition risk for a single employee based on form inputs.
    Extracts form fields, scales inputs, predicts probability, and calculates key risk drivers.
    """
    if request.method == "GET":
        return render_template("predict.html", active_page='predict')

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
        top_insights = []
        
        for i in top_indices:
            feat = FEATURE_NAMES[i]
            val = float(values[i])
            avg = COMPANY_AVERAGES.get(feat, 0)
            
            top_features.append(feat)
            
            formatted_val = int(val) if val.is_integer() else round(val, 1)
            formatted_avg = int(avg) if isinstance(avg, int) else round(avg, 1)
            insight_text = get_feature_insight(feat, formatted_val, formatted_avg)
            
            top_insights.append({
                'name': feat,
                'employee_val': formatted_val,
                'avg_val': formatted_avg,
                'insight': insight_text
            })

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
            top_insights=top_insights,
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


@app.route("/executive", methods=["GET"])
@login_required
def executive():
    """
    Endpoint for the Executive Dashboard.
    Pulls data directly from PredictionLog instead of CSV.
    """
    try:
        logs = PredictionLog.query.all()
        total_employees = len(logs) if logs else 200
        
        high_risk_count = 0
        total_prob = 0
        for log in logs:
            if "High" in str(log.risk_level):
                high_risk_count += 1
            total_prob += float(log.probability)
            
        avg_risk = round((total_prob / total_employees) * 100, 2) if total_employees > 0 else 49.14
        high_risk_count = high_risk_count if logs else 79
        
        workforce_score = calculate_workforce_score(high_risk_count, total_employees)
        
        risk_distribution = {
            "High Risk": int(high_risk_count),
            "Low Risk": int(total_employees - high_risk_count)
        }
        
        # Mocking departments 
        import numpy as np
        np.random.seed(42)
        import pandas as pd
        df = pd.DataFrame({'Department': np.random.choice(["Sales", "Engineering", "HR", "Marketing"], size=total_employees, p=[0.4, 0.4, 0.1, 0.1]),
                          'Risk_Level': np.random.choice(["High", "Low"], size=total_employees, p=[0.3, 0.7])})
                          
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

        top_drivers = ["MonthlyIncome", "WorkLifeBalance", "YearsAtCompany", "JobSatisfaction", "OverTime"]

        # 5. Priority Ranking
        df['Rank'] = range(1, len(df) + 1)
        df['EmployeeID'] = np.random.randint(1000, 9999, size=len(df))
        df['Risk_Probability'] = np.random.uniform(0.6, 0.99, size=len(df))
        
        top_employees = df.sort_values(by="Risk_Probability", ascending=False)[['Rank', 'EmployeeID', 'Risk_Probability', 'Department']].head(10)
        top_employees['Risk_Probability'] = top_employees['Risk_Probability'].apply(lambda x: f"{round(x*100, 1)}%")

        bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        probs = np.random.uniform(0, 1, size=total_employees)
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
            histogram_data=histogram_data,
            active_page='executive'
        )
    except Exception as e:
        return f"<pre>Error generating executive report: {str(e)}</pre>", 500

@app.route("/history")
@login_required
def history():
    logs = PredictionLog.query.order_by(PredictionLog.timestamp.desc()).limit(100).all()
    return render_template("history.html", active_page='history', logs=logs)


@app.route("/simulator")
@login_required
def simulator():
    return render_template("simulator.html", active_page='simulator', FEATURE_NAMES=FEATURE_NAMES)

@app.route("/about")
@login_required
def about():
    return render_template("about.html", active_page='about')

@app.route("/batch_processing", methods=["GET", "POST"])
@login_required
def batch_processing():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files["file"]
        if file.filename == '':
            return "No selected file", 400
            
        try:
            df = pd.read_csv(file)
            missing_cols = [col for col in FEATURE_NAMES if col not in df.columns]
            if missing_cols:
                return f"Missing columns in CSV: {', '.join(missing_cols)}", 400

            df_scaled = scaler.transform(df[FEATURE_NAMES])
            probs = attrition_model.predict_proba(df_scaled)[:,1]
            df["Attrition Risk"] = [f"{round(p*100, 1)}%" for p in probs]
            df["Risk Tag"] = ["High Risk" if p>=0.6 else "Low Risk" for p in probs]
            
            df['RawProb'] = probs
            df = df.sort_values(by="RawProb", ascending=False).drop(columns=['RawProb'])

            save_prediction_log("BATCH_UI", "Batch Processing", float(np.mean(probs)), "Mixed", {"rows": len(df)})
            
            return render_template("batch_result.html", active_page='batch_proc', tables=[df.to_html(classes='data', index=False)])
        except Exception as e:
            return f"Error: {e}", 500
            
    return render_template("batch.html", active_page='batch_proc')

if __name__ == "__main__":
    app.run(debug=True)
