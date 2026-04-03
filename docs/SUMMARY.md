# Project Summary: Employee Attrition Prediction & Retention Engine

## Overview
This project predicts employee attrition (turnover) using machine learning and provides a complete retention engine. It blends academic-level data science with a highly polished, production-ready frontend to deliver clear, actionable insights for HR executives.

## Business Objectives
1.  **Predict Attrition**: Proactively identify employees at high risk of leaving the company.
2.  **Explainability**: Understand *why* an employee is at risk using feature importance/coefficient analysis to find key drivers (e.g., compensation, work-life balance).
3.  **Retention Strategies**: Suggest actionable, targeted interventions to retain high-risk employees before they resign.
4.  **Premium Experience**: Deliver results through a stunning, modern user interface designed for non-technical executive stakeholders.

## Current Status (Frontend & Metrics Completed)
### Infrastructure & Data Pipeline
*   **Infrastructure**: Project structure, modular scripts (`src/`), and comprehensive documentation (`docs/`) established.
*   **Data Pipeline**: Preprocessing pipeline including label encoding and standard scaling is fully functional (`src/data_preprocessing.py`).

### Machine Learning Models & Success Rates
*   **Baseline Model (Logistic Regression)**:
    *   **Accuracy**: **88%**
    *   **Performance**: 86% weighted average precision and a 93% F1-score for retained employees.
    *   **Use Case**: Fast, linear, easily explainable real-time inference in the web app.
*   **Advanced Model (Random Forest)**:
    *   **Performance**: Superior non-linear pattern recognition.
    *   **Use Case**: Used by the backend Retention Engine (`src/retention_engine.py`) for deep feature importance analysis to identify top organizational drivers of attrition.

### Web Application & UI
*   A complete Flask API (`app/app.py`) is deployed locally.
*   A visually stunning, modern HTML/CSS interface has been built. It features a premium design system, interactive forms, responsive data tables, and an Executive Dashboard.
*   Supports single-prediction (manual entry) and batch CSV processing (`/batch`).

## Next Steps
*   **Login System**: Add authentication for secure HR access.
*   **CI/CD Pipeline**: Write automated tests and deploy to a cloud provider like Render, Heroku, or AWS.
*   **Database Integration**: Swap out CSV parsing for a true SQL backend (e.g., PostgreSQL) for persistent employee records.
