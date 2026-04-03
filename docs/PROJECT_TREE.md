# Project Structure

```
employee-attrition-ai/
│
├── app/                        # [NEW] Web Application
│   ├── static/
│   │   └── style.css           # Professional HR styling
│   ├── templates/
│   │   ├── index.html          # Main dashboard for single assessment
│   │   ├── result.html         # Individual risk result breakdown
│   │   ├── batch_result.html   # Generic Batch upload results
│   │   ├── executive_upload.html # CSV Upload for executive view
│   │   └── executive.html      # Leadership dashboard
│   └── app.py                  # Flask backend logic
│
├── data/
│   └── employee_attrition.csv  # IBM HR Dataset (not in tracking)
│
├── docs/
│   ├── DEVELOPMENT_STEPS.md    # Step-by-step dev log
│   ├── FILE_DESCRIPTIONS.md    # Exhaustive file detail
│   ├── HOW_TO_RUN.md           # Setup and execution guide
│   ├── PROJECT_TREE.md         # This file
│   ├── REQUIREMENTS.md         # Detailed dependency logic
│   └── SUMMARY.md              # High-level overview
│
├── models/
│   ├── attrition_model.pkl     # Trained Logistic Regression
│   ├── rf_model.pkl            # Trained Random Forest
│   ├── scaler.pkl              # Saved StandardScaler
│   └── feature_importance.png  # Visual chart of attrition factors
│
├── src/                        # [PHASE 1] Core ML Logic
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── requirements.txt
└── README.md
```
