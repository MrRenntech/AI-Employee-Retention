# Project Requirements

This project requires Python 3.8+ and the following libraries:

## Web Framework
*   **flask**: A lightweight WSGI web application framework. Used to serve the model as an API.

## Core Data Science Libraries
*   **pandas**: Used for data manipulation and analysis, specifically for loading the CSV dataset and handling dataframes.
*   **numpy**: fundamental package for scientific computing with Python, used for numerical operations.

## Machine Learning & Statistics
*   **scikit-learn**: The primary machine learning library used for:
    *   `LabelEncoder`: To convert categorical text data into numbers.
    *   `StandardScaler`: To scale features for better model performance.
    *   `train_test_split`: To split data into training and testing sets.
    *   `LogisticRegression`: The baseline classification model.
    *   `metrics`: For calculating accuracy, confusion matrices, and classification reports.
*   **joblib**: Used for saving (`dump`) and loading (`load`) trained models and scalers to/from the disk.

## Visualization
*   **matplotlib**: Used for creating static, animated, and interactive visualizations.
*   **seaborn**: A Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Installation
To install all requirements, run:
```bash
pip install -r requirements.txt
```
