# How to Run the Employee Attrition Prediction Project

Follow these steps to set up and run the baseline model.

## Prerequisites
1.  Ensure you have **Python 3.8+** installed.
2.  Ensure you have the repository cloned or downloaded.

## Step 1: Install Dependencies
Open your terminal (Command Prompt or PowerShell) and navigate to the project root:
```bash
cd "e:\Projects\AI Employee\employee-attrition-ai"
```

**Highly Recommended: Create a Virtual Environment**
Creating a virtual environment isolates your project dependencies from other Python installations on your system.
```bash
python -m venv venv
```

**Activate the Virtual Environment:**
*   **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
*   **Windows (Command Prompt):** `.\venv\Scripts\activate.bat`
*   **Mac/Linux (Bash):** `source venv/bin/activate`

Once activated (you should see `(venv)` in your prompt), install the required Python packages:
```bash
pip install -r requirements.txt
```

## Step 2: Prepare the Data
Ensure the dataset exists at `data/employee_attrition.csv`.
*   If missing, download the **IBM HR Analytics Employee Attrition Dataset** and place it there.

## Step 3: Train the Model
Run the training script to preprocess data, train the Logistic Regression model, and save the artifacts (`attrition_model.pkl` and `scaler.pkl`).

**Important**: You must set the `PYTHONPATH` to include the `src` directory so imports work correctly.

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python src/train_model.py
```

**Command Prompt (cmd):**
```cmd
set PYTHONPATH=src && python src/train_model.py
```

**Bash (Linux/Mac):**
```bash
PYTHONPATH=src python src/train_model.py
```

*Troubleshooting*: If you still encounter `ModuleNotFoundError: No module named 'src'`, ensure you are actively running the command from the root folder (`employee-attrition-ai`) and not from within `src` itself.

Expected Output:
```
Baseline Accuracy: 0.88...
Baseline model saved.
```

## Step 4: Evaluate the Model
Run the evaluation script to see the Confusion Matrix and Classification Report.

**Windows PowerShell:**
```powershell
$env:PYTHONPATH="src"; python src/evaluate_model.py
```

Expected Output:
*   A confusion matrix showing True Positives, True Negatives, False Positives, and False Negatives.
*   A detailed classification report with Precision, Recall, and F1-Score.

## Step 5: Advanced Model (Retrain with Random Forest)
To improve accuracy and get feature importance, run the Random Forest script.
```powershell
$env:PYTHONPATH="src"; python src/train_model_rf.py
```
This will save `models/rf_model.pkl` and generating `models/feature_importance.png`.

## Step 6: Run Retention Engine
To identify high-risk employees and see suggested interventions:
```powershell
$env:PYTHONPATH="src"; python src/retention_engine.py
```
Expected Output:
*   Count of high-risk employees found.
*   Detailed list of sample cases with recommended actions (e.g., "Schedule 1-on-1", "Review compensation").

## Step 7: Run the Flask API (Deployment)
To start the REST API server:
```powershell
$env:PYTHONPATH="src"; python app/app.py
```
You should see: `Running on http://127.0.0.1:5000`

### Testing the API
You can test it using **Postman** or **curl**.

**Example CURL request (Windows CMD/PowerShell requires escaping inner quotes, or use Postman for ease):**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 29, \"DailyRate\": 1100, \"DistanceFromHome\": 5, \"Education\": 3, \"EnvironmentSatisfaction\": 2, \"HourlyRate\": 70, \"JobInvolvement\": 2, \"JobLevel\": 2, \"JobSatisfaction\": 2, \"MonthlyIncome\": 4200, \"MonthlyRate\": 20000, \"NumCompaniesWorked\": 3, \"PercentSalaryHike\": 11, \"PerformanceRating\": 3, \"RelationshipSatisfaction\": 2, \"StockOptionLevel\": 0, \"TotalWorkingYears\": 6, \"TrainingTimesLastYear\": 2, \"WorkLifeBalance\": 2, \"YearsAtCompany\": 3, \"YearsInCurrentRole\": 2, \"YearsSinceLastPromotion\": 2, \"YearsWithCurrManager\": 2}" http://127.0.0.1:5000/predict
```

**Expected JSON Response:**
```json
{
  "attrition_risk": "High Risk",
  "risk_probability": 0.71,
  "top_risk_factors": ["MonthlyIncome", "WorkLifeBalance", "YearsSinceLastPromotion"],
  "recommended_actions": ["Review compensation", "Improve work-life balance"]
}
```
