<div align="center">
  
# 🧠 RetentionAI: Enterprise Employee Attrition Engine

[![Live Deployment](https://img.shields.io/badge/Live_Deployment-Up_%26_Running-success?style=for-the-badge&logo=render)](https://ai-employee-retention.onrender.com/)
[![Python Requirements](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask Web Framework](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

**A Production-Ready AI Suite for Proactive HR Decision Making.**

---

</div>

## 🌐 Live Application
The fully functional production application is currently live on Render:
👉 **[Access RetentionAI Here](https://ai-employee-retention.onrender.com/)**

*(For security and system health, the app requires authentication. If deployed locally, you can initialize the DB using `python app/init_db.py` to generate the default `admin`/`password` account.)*

---

## 📖 Project Overview
Traditional HR systems rely on reactive measures—like exit interviews—to understand why employees resign. By that time, the talent has already left. **RetentionAI** completely inverts this paradigm by shifting HR into a proactive, data-driven framework.

By ingesting raw metrics (like salary, commute distance, stock options, and job satisfaction) from the IBM HR Analytics dataset, this system computes an exact mathematical risk percentage of impending employee resignation. 

More importantly, it provides **Explainable AI**. Instead of a "black box" prediction, the system acts as a Retention Engine, translating the algorithm's coefficients into concrete English recommendations (e.g., "Schedule a career growth 1-on-1", "Review compensation structure").

## 🚀 Key Features

*   **Dual Machine Learning Architecture**: 
    *   **Baseline API Model:** 88% accurate Logistic Regression model allowing fast, linear, highly explainable real-time inferences.
    *   **Advanced Analytical Model:** Deep Random Forest algorithm analyzing nonlinear patterns to map exactly which corporate systemic issues are causing attrition.
*   **Executive Dashboard**: A premium, visually stunning web UI featuring Glassmorphism design aesthetics, allowing non-technical HR leaders to consume AI metrics instantly.
*   **Batch Roster Processing**: Instead of single entries, executives can drag-and-drop massive `.csv` files into the portal to generate an instant triage list ranking hundreds of employees by flight risk.
*   **Bank-Grade Security**: Fully guarded via `Flask-Login` session management, utilizing `werkzeug pbkdf2:sha256` password hashing to protect sensitive HR data.
*   **Persistent Historical Auditing**: Seamless `Flask-SQLAlchemy` (SQLite) integration ensures every single interaction and risk profile is permanently logged for HR auditing and efficacy tracking over time.

---

## 🛠️ Technology Stack

| Domain | Tools Used |
| :--- | :--- |
| **Machine Learning** | `scikit-learn`, `numpy`, `pandas`, `joblib` |
| **Web Framework** | `Flask`, `Flask-Login`, `Flask-SQLAlchemy` |
| **Frontend/UI** | `HTML5`, Vanilla CSS, `Chart.js` |
| **Production/DevOps** | `Gunicorn`, `Docker`, `Pytest`, `GitHub Actions (CI/CD)` |

---

## 🏗️ Architecture & Deployment

This application is rigorously structured to bypass the typical "Jupyter Notebook" data science portfolio standard, instead matching modern software engineering architecture:

1. **Source Code (`src/`)**: Isolated Machine Learning scripts for automated cleaning, preprocessing (`StandardScaler`, `LabelEncoder`), modeling, and evaluation.
2. **Web API (`app/`)**: Flask route handlers, UI templates, and SQLAlchemy data models.
3. **CI/CD (`.github/workflows`)**: Automated robot unit testing via Pytest that acts as a secure merge-gate for the repository.

To deploy this yourself (AWS, Render, Heroku): it comes pre-packaged with a `Dockerfile`, a `.dockerignore`, `runtime.txt`, and a `Procfile` configured for the multi-threaded `gunicorn` WSGI server. 

### Local Execution
```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Boot up the Database (Creates initial database and Admin account)
python app/init_db.py

# 3. Launch the Server!
python -m app.app
```
*Application runs on http://127.0.0.1:5000*
