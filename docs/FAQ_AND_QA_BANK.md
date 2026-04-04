# ❓ Presentation FAQ & QA Bank

*(Instructions for Presenter: Keep this document open during your Q&A session. It contains highly detailed answers to anticipated audience questions regarding both business value and technical architecture.)*

---

## 🏢 Business & HR Questions

### Q1: Is this AI biased against certain groups?
*   **Answer**: Great question. This is exactly why we prioritized **Explainable AI** over "black box" models. Our algorithm explicitly breaks down the driving factors for every single prediction. If the model flags someone as a flight risk, it tells us exactly *why* (e.g., "Commute distance is too long" + "No promotion in 4 years"). Because we can read the model's logic directly, human HR professionals remain in the loop to audit the results and ensure fairness.

### Q2: What exactly do we do when an employee is flagged as "High Risk"?
*   **Answer**: The system doesn't just predict; it prescribes. The dashboard features a "Retention Engine" that outputs English advice (e.g., "Schedule a career growth 1-on-1", "Review compensation structure"). HR leadership should use this list as a prioritized triage queue for manager interventions. 

### Q3: What happens if our company changes next year and new patterns emerge?
*   **Answer**: The AI is designed to continuously learn. If our underlying dynamics change, we simply push the newest HR dataset through our retraining script (`train_model.py`). The model adjusts its weights to understand the new reality, and the web portal instantly updates without any downtime.

---

## 💻 Technical Questions

### Q4: Why did we use Logistic Regression and Random Forest instead of Neural Networks?
*   **Answer**: Enterprise HR data requires **Interpretability**. Deep Learning (Neural Networks) acts as a black box—it might give a great prediction, but it can't tell you *why*. We chose Logistic Regression for our real-time API because it provides linear, highly interpretable coefficients. We supplemented it with a Random Forest model for deep, non-linear insights regarding feature importance. This dual-architecture guarantees both speed and absolute transparency.

### Q5: How secure is the HR data inside this application?
*   **Answer**: Security is our highest priority. The portal is protected by `Flask-Login` session management—meaning unauthenticated URLs bounce entirely. Furthermore, all accounts are stored in our SQLite database using `werkzeug pbkdf2:sha256` password hashing. Even if the database were physically stolen, the passwords remain cryptographically unreadable.

### Q6: Can this scale to thousands of employees?
*   **Answer**: Yes. Our backend relies on `pandas` and `numpy` for C-level mathematical processing. When you upload a batch `.csv` roster, the server vectorizes the data and processes thousands of predictions in milliseconds. 

### Q7: If a new engineer joins the team, how do they safely update the codebase?
*   **Answer**: We have a strict CI/CD pipeline integrated with GitHub Actions. Any new code must pass our automated `pytest` robotic QA suite. These invisible bots boot up the server, attempt to log in using fake credentials, and test the ML models. If the code breaks the site, it is automatically rejected before it ever reaches production.
