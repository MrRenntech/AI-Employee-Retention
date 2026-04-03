# Complete Project Structure Tree

Here is the exact layout of the entire system as it currently exists on your computer.

```text
employee-attrition-ai/
│
├── .github/                    # Automated GitHub CI/CD Workflows
│   └── workflows/
│       └── ci.yml              # Instructs GitHub to run our auto-tests securely
│
├── app/                        # The Web Server Application (Powered by Flask)
│   ├── static/
│   │   └── style.css           # Premium styling, colors, and layout instructions
│   │
│   ├── templates/              # The HTML Web Pages
│   │   ├── index.html          # Main hub / assessment dashboard
│   │   ├── login.html          # Secure entry gateway for HR
│   │   ├── history.html        # Table view for the Database logs
│   │   ├── result.html         # One-on-one individual risk analysis screen
│   │   ├── batch_result.html   # Generic CSV output spreadsheet
│   │   ├── executive_upload.html # Drag-and-drop CSV box for Executives
│   │   └── executive.html      # Beautiful charts summarizing company health
│   │
│   ├── app.py                  # The main program! Connects AI, Database, and Web.
│   ├── init_db.py              # Run this ONCE to build a blank SQLite Database.
│   └── models.py               # Defines how "Users" and "Prediction Logs" are stored.
│
├── data/                       # Contains our Spreadsheets
│   ├── employee_attrition.csv  # IBM HR Dataset (Base Reality Data)
│   └── fake_employee_dataset.csv # 2000 fake humans generated for safe testing
│
├── docs/                       # The Documentation Library (You are here!)
│   ├── DEVELOPMENT_STEPS.md    
│   ├── FILE_DESCRIPTIONS.md    
│   ├── HOW_TO_RUN.md           
│   ├── PROJECT_TREE.md         
│   ├── REQUIREMENTS.md         
│   └── SUMMARY.md              
│
├── models/                     # The Sleeping AI Brains (Serialized files)
│   ├── attrition_model.pkl     # Logistic Regression Model (Saved)
│   ├── rf_model.pkl            # Random Forest Model (Saved)
│   ├── scaler.pkl              # Mathematical data-squisher (Saved)
│   └── feature_importance.png  # Simple image exporting AI logic
│
├── src/                        # Machine Learning Lab (Data Science Zone)
│   ├── data_preprocessing.py   # Cleans dirty data into math
│   ├── train_model.py          # Trains the basic AI
│   ├── train_model_rf.py       # Trains the advanced AI
│   ├── evaluate_model.py       # Grades the AI
│   ├── retention_engine.py     # Writes English advice based on math
│   └── generate_fake_dataset.py# Python script creating fake test data
│
├── tests/                      # Automated Quality Assurance (QA Robots)
│   ├── test_app.py             # Robot clicks around website to find bugs
│   └── test_model.py           # Robot checks if ML files exist and load properly
│
├── requirements.txt            # The Shopping List of Python downloads needed
└── README.md                   # Your front-page cover project summary!
```
