# Project Structure

```
employee-attrition-ai/
│
├── app/                        # [NEW] Web Application
│   ├── static/
│   │   └── style.css           # Professional HR styling
│   ├── templates/
│   │   ├── index.html          # Main dashboard
│   │   ├── result.html         # Individual risk result
│   │   └── batch_result.html   # Batch upload results
│   └── app.py                  # Flask backend logic
│
├── data/
│   └── employee_attrition.csv  # IBM HR Dataset
│
├── docs/
│   ├── PROJECT_TREE.md         # This file
│   └── DEVELOPMENT_STEPS.txt   # Step-by-step dev log
│
├── models/
│   ├── attrition_model.pkl     # Trained Logistic Regression
│   └── scaler.pkl              # Saved StandardScaler
│
├── src/                        # [PHASE 1] Core ML Logic
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── requirements.txt
└── README.md
```
