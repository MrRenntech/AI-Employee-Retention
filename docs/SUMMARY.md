# Project Summary: Employee Attrition Prediction & Retention Engine

## Overview
This project predicts employee attrition (turnover) using machine learning and provides a complete retention engine. It blends academic-level data science with a highly polished, production-ready frontend to deliver clear, actionable insights for HR executives.

## Objectives
1.  **Predict Attrition**: Identify employees at risk of leaving the company.
2.  **Explainability**: Understand *why* an employee is at risk using feature importance.
3.  **Retention Strategies**: Suggest actionable steps to retain high-risk employees.
4.  **Premium Experience**: Deliver results through a stunning, modern user interface.

## Current Status (Frontend & Metrics Completed)
*   **Infrastructure**: Project structure and documentation established.
*   **Data Pipeline**: Preprocessing pipeline including encoding and scaling is fully functional (`src/data_preprocessing.py`).
*   **Models Details & Success Rate**:
    *   **Baseline (Active)**: Logistic Regression achieving **88% Accuracy**. The model has an 86% weighted average precision and a 93% F1-score for retained employees.
    *   **Advanced**: Random Forest model implementation is available (`src/train_model_rf.py`), providing potentially higher precision and non-linear feature analysis.
*   **Explainability**: Implemented feature importance analysis to identify key drivers of attrition per employee.
*   **Frontend & Web App**:
    *   A complete Flask API (`app/app.py`) is deployed locally.
    *   A visually stunning, modern HTML/CSS interface has been built. It features a premium design system, interactive forms, responsive data tables, and an Executive Dashboard.
    *   Supports single-prediction and batch CSV processing.

## Next Steps
*   **Login System**: Add authentication for secure access.
*   **CI/CD Pipeline**: Write automated tests and deploy to a cloud provider like Render or AWS.
*   **Database Integration**: Swap out CSV parsing for a true SQL backend for persistent employee records.
