# 🚀 Live Demo & Presentation Guide

*(Instructions for Presenter: Follow this script step-by-step to execute a flawless live demonstration of the software during your presentation.)*

---

## Part 1: Booting Up (Do this BEFORE presenting)
1. Ensure you have Python installed.
2. Open your terminal and navigate to the project root:
   ```bash
   cd e:\Projects\AI Employee\employee-attrition-ai
   ```
3. *(If you haven't yet, initialize the database)*
   ```bash
   python app/init_db.py
   ```
4. Start the Application Server:
   ```bash
   python -m app.app
   ```
5. Open your web browser and load: `http://127.0.0.1:5000`

---

## Part 2: The Live Presentation Script

### 1. The Welcome & Login
*   **Action**: Show the Login Screen.
*   **Script**: *"Welcome to the Apex Analytics secure portal. Because HR data is incredibly sensitive, the entire application sits behind a secure Flask-Login wall. I'm going to log in with our encrypted Admin credentials."*
*   **Action**: Enter `admin` / `password` and hit Login.

### 2. Individual Assessment Demonstration
*   **Action**: Land on the main Assessment Dashboard.
*   **Script**: *"As you can see, the UI is built entirely for executives—clean, modern, and intuitive. Let's say I'm a manager and I have a bad feeling about a specific employee."*
*   **Action**: Fill out the Single Employee Form with high-risk metrics (Low Salary, Low Satisfaction, High Commute). Click Predict.
*   **Script**: *"Instead of guessing, the AI instantly computes their exact mathematical flight risk. More importantly, it explains the underlying causes and prescribes an actionable, English-language retention strategy."*

### 3. The Batch Roster Upload (The "Wow" Moment)
*   **Action**: Navigate back to the Dashboard. Click the "Batch Assessment" tab.
*   **Script**: *"Now, analyzing one person is great, but companies have thousands of employees. Our tool allows complete scale."*
*   **Action**: Open your file explorer. Drag and drop the `data/ai_based_dataset.csv` file into the portal.
*   **Script**: *"I'm uploading our test roster now. The AI is vectorizing thousands of data points..."*
*   **Action**: Show the massive sorted output table.
*   **Script**: *"In less than a second, it has analyzed the entire spreadsheet and generated an emergency triage list. The leadership team can immediately prioritize those ranking at 85%+ risk."*

### 4. Executive View & History
*   **Action**: Click on the "Executive Dashboard" or "Database History" tab.
*   **Script**: *"Finally, every single prediction we run is persistently saved into a secure SQLite database, allowing total historical auditing and tracking. We can view broad, company-wide trends with dynamic charts."*
