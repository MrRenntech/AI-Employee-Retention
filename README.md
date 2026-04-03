<p align="center">
  <img src="https://raw.githubusercontent.com/MrRenntech/AI-Employee-Retention/main/app/static/favicon.ico" width="100" />
</p>

<h1 align="center">🌟 RetentionAI: Employee Attrition Prediction 🌟</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Model%20Accuracy-88%25-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge" />
</p>

<p align="center">
  <i>An advanced AI-powered HR analytics tool designed to predict employee attrition risk and provide actionable retention interventions.</i>
</p>

---

## 🚀 Project Overview
RetentionAI transforms raw HR metrics into clear, actionable intelligence. It utilizes an **88% accurate** Logistic Regression machine learning model (baseline) and an Advanced Random Forest model integrated into a meticulously designed, beautiful Flask web interface. The system identifies high-risk employees instantly and suggests tailored retention strategies based on individual risk drivers.

## ✨ Key Features
- 🧠 **Precision Machine Learning**: Achieves an **88% baseline accuracy** (93% F1-score for retention) with Logistic Regression, and supports an advanced Random Forest model for non-linear feature analysis.
- 💎 **Premium Web Dashboard**: A stunning, modern UI built with custom CSS, glassmorphism, responsive data grids, and smooth animations.
- 🎯 **Individual Assessments**: Predict a single employee's risk instantly by inputting metrics directly into the aesthetic form.
- 🗂️ **Batch Processing Engine**: Upload organizational `.csv` rosters to dynamically rank hundreds of employees by attrition probability.
- 📊 **Executive Dashboard**: A sleek high-level overview detailing aggregate risk distributions and systemic organizational drivers.

For full details on the machine learning models and performance metrics, please read the [Project Summary (`docs/SUMMARY.md`)](docs/SUMMARY.md).

---

## 📂 Project Architecture
```graphql
employee-attrition-ai/
├── app/                    # 🌐 Web Application (Flask)
│   ├── static/             # 🎨 Modern CSS styles & Assets
│   ├── templates/          # 📄 Responsive HTML templates
│   └── app.py              # ⚙️ Routing & Model Inference API
├── data/                   # 📊 Dataset storage (Ignored in Git)
├── docs/                   # 📚 Detailed Architecture & Walkthroughs
├── models/                 # 🧠 Serialized ML formats (attrition_model.pkl)
├── notebooks/              # 📓 Jupyter notebooks for EDA
└── src/                    # 🛠️ Data pipeline and Training scripts
```
*For a detailed breakdown of every file, please refer to [File Descriptions (`docs/FILE_DESCRIPTIONS.md`)](docs/FILE_DESCRIPTIONS.md).*

---

## ⚙️ Quick Start Guide

### 1. Installation
Clone the repository and install dependencies (a virtual environment is highly recommended):
```bash
git clone https://github.com/MrRenntech/AI-Employee-Retention.git
cd AI-Employee-Retention
python -m venv venv
# Activate the virtual environment:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```
*For detailed installation requirements, see [Requirements (`docs/REQUIREMENTS.md`)](docs/REQUIREMENTS.md).*

### 2. Model Training (First Run)
Before booting the dashboard, compile the machine learning artifacts:
```bash
# Ensure you are in the project root and then run:
python src/train_model.py
```
*(Generates the serialized model and scaler securely in the `/models` directory).*
*For detailed instructions on running all aspects of the project, including advanced models, see the complete [How to Run Guide (`docs/HOW_TO_RUN.md`)](docs/HOW_TO_RUN.md).*

### 3. Launching the App
Start the Flask web server:
```bash
python app/app.py
```
🌐 **Open your browser and navigate to:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 How It Works
- **Data Preprocessing**: Categorical features are encoded and numerical features scaled via `StandardScaler` to ensure optimal gradient descent.
- **Explainability**: The system unpacks model coefficients to pinpoint exactly *why* a specific employee might leave (e.g., *Compensation*, *Distance from Home*, or *Environment Satisfaction*).

---

<p align="center">
  <i>Developed with ❤️ for intelligent HR management.</i>
</p>
