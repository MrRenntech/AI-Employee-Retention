# 🏗️ Architecture & Technology Justification

*(Instructions for Presenter: Use this document to definitively answer any questions regarding WHY specific tools were chosen, and HOW data flows securely through our system.)*

---

## 1. The Machine Learning Engine (Scikit-Learn)
We chose **Scikit-Learn** powered by `numpy` and `pandas` for our core data science tier. 
*   **Why?** Enterprise HR requires *Explainable AI*. Black box deep learning algorithms (like Neural Networks) cannot easily articulate why they made a decision. 
*   **The Baseline Model (Logistic Regression)** provides mathematically sound, linear coefficients that highlight exactly which features push an employee towards resigning. 
*   **The Advanced Model (Random Forest)** provides sophisticated non-linear analysis, capturing complex interactions between departments and salaries. 
*   These tools vectorize massive data pipelines (`StandardScaler`, `LabelEncoder`) instantly and serialize perfectly via `joblib`.

## 2. The Application Tier (Flask)
We selected **Flask** as the primary Web Framework.
*   **Why?** The project required blending hard python Data Science scripts with an accessible web frontend. Flask natively integrates with Python, circumventing the need for complex microservices. It is lightweight, scalable via `Gunicorn`, and seamlessly calls our saved `.pkl` AI brains within millisecond response times.

## 3. Data Persistence (SQLite & SQLAlchemy)
We utilize **SQLite** managed dynamically via **Flask-SQLAlchemy**.
*   **Why?** A key requirement was historical auditing. SQLAlchemy allows us to manage database objects purely in Python, ignoring messy SQL logic. SQLite stores the entire prediction log securely as a localized file, making the entire application highly portable (easy to deploy on containerized hosting without spinning up a separate AWS RDS server).

## 4. UI & Aesthetics (Glassmorphism & Chart.js)
*   **Why?** A tool is only valuable if non-technical executives enjoy using it. We built the frontend with modern HTML5, vanilla CSS utilizing "Glassmorphism" design patterns (blur effects, gradients, soft shadows), and `Chart.js` for dynamic, rendering visual data. This delivers an expensive, premium "SaaS" feel directly out of the box.

## 5. Automated CI/CD (Pytest & GitHub Actions)
*   **Why?** High-quality production software cannot crash. We implemented `Pytest` to programmatically build robot agents that mimic human users, log into the site, and verify the AI predictions. This is connected to a GitHub Action (`ci.yml`) that acts as an automated firewall, rejecting flawed code before it ever reaches the live server.
