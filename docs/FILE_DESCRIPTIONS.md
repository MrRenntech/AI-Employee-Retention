# 📂 File Flow & Descriptions

*(Instructions for Presenter: Ensure you understand how files interconnect. This guide details exactly HOW data moves through the project tree.)*

---

## 1. The Entry Point: Web Architecture (`app/`)
This module commands the user interface.

*   **`app/app.py`**: The Central Nervous System. It boots the Flask Web Server, manages login sessions, reads form/CSV data, dynamically loads `models/attrition_model.pkl` to fetch predictions, and injects the results back to the user interface.
*   **`app/models.py`**: The Database Blueprint (SQLAlchemy). It structures exactly how HR Users and Prediction Audit Logs are securely formatted for the database.
*   **`app/init_db.py`**: The Initializer. Run this script once to mint the database architecture and generate your secure Admin login.
*   **`app/templates/*.html`**: The UI rendering engines (Index, Results, Executive Dashboards).
*   **`app/static/style.css`**: The premium styling components.

## 2. The Data Science Engine (`src/`)
This module operates strictly behind the scenes to train the models *before* the web application ever runs.

*   **`src/data_preprocessing.py`**: The Data Sanitizer. It digests messy HR CSV data, removes noise, mathematically normalizes scales (using `StandardScaler`), and encodes text (using `LabelEncoder`).
*   **`src/train_model.py`**: The Machine Learning Factory. It pushes cleaned data through a Logistic Regression algorithm, tuning the math until accuracy reaches 88%. It saves this optimal "brain" as `attrition_model.pkl`.
*   **`src/train_model_rf.py`**: The deep-analyzer that builds a Random Forest model.
*   **`src/retention_engine.py`**: The Translator. Maps raw AI coefficients to actionable English commands (e.g. mapping "high commute distance" to "Provide flexible work hours").
*   **`src/generate_fake_dataset.py`**: A simulator generating thousands of synthetic, randomized testing profiles (`ai_based_dataset.csv`).

## 3. The Security & Validation Modules (`tests/` & `.github/`)
*   **`tests/test_model.py` & `tests/test_app.py`**: Programmed QA bots that stress-test both the models and the web endpoints to ensure the code remains stable.
*   **`.github/workflows/ci.yml`**: The invisible cloud engineer. When code is pushed to the repo, it boots a dedicated Linux server to run all the tests above, blocking failing code immediately.

## 4. The Assets (`data/` & `models/`)
*   **`data/`**: Holds CSV files. `ibm_dataset.csv` is the initial training ground, while `ai_based_dataset.csv` acts as our high-speed batch testing group.
*   **`models/`**: The Serialized output folder. Files like `attrition_model.pkl` reside here so they can be instantaneously loaded by the server without re-training.
