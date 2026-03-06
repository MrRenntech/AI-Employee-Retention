# File Descriptions

This document explains the purpose and functionality of each file in the project.

## Root Directory
*   `requirements.txt`: Lists all Python code dependencies required to run the project.
*   `README.md`: General project overview (to be created).

## `app/` (Deployment)
*   **`app.py`**:
    *   **Purpose**: A lightweight Flask web server acting as the prediction API.
    *   **Logic**:
        *   Loads the trained Random Forest model (`rf_model.pkl`) and scaler (`scaler.pkl`).
        *   Defines a `/predict` endpoint (POST).
        *   Accepts JSON data representing an employee.
        *   Returns JSON with Attrition Risk (High/Low), Probability, Top Risk Factors, and Recommended Actions.

## `src/` (Source Code)
*   **`data_preprocessing.py`**:
    *   **Purpose**: Handles all data cleaning and transformation tasks.
    *   **Key Functions**: `load_and_preprocess(path)`
    *   **Logic**:
        *   Loads CSV data.
        *   Drops irrelevant columns (e.g., `EmployeeNumber`).
        *   Encodes the target variable `Attrition` (Yes=1, No=0).
        *   Encodes categorical features using `LabelEncoder`.
        *   Scales numerical features using `StandardScaler`.
        *   Returns processed features (`X`), target (`y`), the fitted `scaler`, and feature names.

*   **`train_model.py`**:
    *   **Purpose**: Trains the machine learning model (Logistic Regression Baseline).
    *   **Logic**:
        *   Imports preprocessing logic.
        *   Splits data into training/testing sets.
        *   Trains a Logistic Regression model.
        *   Saves artifacts to `models/`.

*   **`train_model_rf.py`**:
    *   **Purpose**: Trains the advanced Random Forest model.
    *   **Logic**:
        *   Trains a `RandomForestClassifier`.
        *   Evaluates accuracy (typically higher than baseline).
        *   Calculates **Feature Importance** (what drives attrition).
        *   Saves the model to `models/rf_model.pkl`.
        *   Generates and saves a feature importance plot to `models/feature_importance.png`.

*   **`evaluate_model.py`**:
    *   **Purpose**: Evaluates the trained model's performance on the full dataset (or test set).
    *   **Logic**:
        *   Loads the saved model (`attrition_model.pkl`).
        *   Predicts attrition on the dataset.
        *   Prints a **Confusion Matrix** and **Classification Report**.

*   **`retention_engine.py`**:
    *   **Purpose**: The core logic for identifying high-risk employees and suggesting interventions.
    *   **Logic**:
        *   Loads the advanced Random Forest model.
        *   Calculates attrition probability for employees.
        *   Identifies "High Risk" employees (Prob > 70%).
        *   Suggests targeted interventions (e.g., "Review Compensation").

## `data/`
*   `employee_attrition.csv`: The raw input dataset containing employee records.

## `models/`
*   `attrition_model.pkl`: The serialized (saved) trained Logistic Regression model.
*   `rf_model.pkl`: The serialized (saved) trained Random Forest model.
*   `scaler.pkl`: The serialized StandardScaler object used to normalize input data.
*   `feature_importance.png`: Visual chart of top attrition factors.

## `docs/`
*   Contains all project documentation.
