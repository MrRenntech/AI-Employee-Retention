# Project Summary: Employee Attrition Prediction & Retention Engine

## Overview
This project aims to predict employee attrition (turnover) using machine learning and provides a retention engine to suggest interventions. It is designed to be a clean, disciplined, and faculty-safe implementation suitable for academic evaluation.

## Objectives
1.  **Predict Attrition**: Identify employees at risk of leaving the company.
2.  **Explainability**: Understand *why* an employee is at risk (Feature Importance).
3.  **Retention Strategies**: Suggest actionable steps to retain high-risk employees.

## Current Status (Phase 3 Complete)
*   **Infrastructure**: Project structure and documentation established.
*   **Data Pipeline**: Preprocessing pipeline including encoding and scaling is fully functional.
*   **Models**:
    *   **Baseline**: Logistic Regression (~88% accuracy).
    *   **Advanced**: Random Forest (Higher accuracy, usually >85%).
*   **Explainability**: Feature importance analysis identifying key drivers of attrition.
*   **Retention Engine**: Operational script identifying high-risk employees and suggesting interventions.
*   **Deployment**: A Flask API (`app/app.py`) is implemented to serve real-time predictions.

## Next Steps
*   **Frontend**: Build a web interface (likely Flask templating or Streamlit) to visualize the API results.
*   **Login System**: Add authentication for secure access.

