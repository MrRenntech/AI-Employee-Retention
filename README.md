# Employee Attrition Prediction AI

## Project Overview
This project is an AI-powered HR analytics tool designed to predict employee attrition risk. It uses machine learning to identify high-risk employees and provides actionable retention recommendations.

## Features
- **Machine Learning Model**: Logistic Regression model trained on IBM HR Analytics data.
- **Web Dashboard**: Clean, professional Flask-based interface for HR use.
- **Individual Assessment**: Form-based input to assess single employee risk.
- **Batch Processing**: Upload CSV files to assess risk for multiple employees at once.
- **Risk Explainability**: Identifies top driving factors for attrition risk.
- **Actionable Insights**: Provides specific retention strategies based on risk factors.

## Project Structure
```
employee-attrition-ai/
├── app/                    # Web Application
│   ├── static/             # CSS and assets
│   ├── templates/          # HTML templates
│   └── app.py              # Flask backend
├── data/                   # Dataset storage
├── docs/                   # Documentation
├── models/                 # Serialized ML models
├── notebooks/              # Jupyter notebooks for exploration
├── src/                    # Data processing and training scripts
└── requirements.txt        # Python dependencies
```

## Setup & Installation
1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd employee-attrition-ai
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Train the Model (First Run Only)
Before running the dashboard, ensure the model is trained and saved:
```bash
python src/train_model.py
```
This generates `attrition_model.pkl` and `scaler.pkl` in the `models/` directory.

### 2. Run the Dashboard
Launch the web application:
```bash
python app/app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

### 3. Using the Dashboard
- **Individual Prediction**: Enter employee details in the form to get a risk assessment.
- **Batch Upload**: Upload the `data/employee_attrition.csv` file (or similar) to see a ranked list of at-risk employees.

## Requirements
- Python 3.8+
- Flask
- Pandas, NumPy, Scikit-learn
- Joblib
