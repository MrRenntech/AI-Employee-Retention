# Project File Descriptions 📂

Welcome to the heart of the project! This document serves as your ultimate guide to understanding what every single file in this project does. Think of it as the blueprints to a finely tuned machine.

---

## The Root Folder (Where Everything Starts)
These files sit at the base of the folder and prepare the environment before any code runs.

*   `requirements.txt`: This is our grocery list! It tells Python exactly which external libraries it needs to download to make our code work (like `pandas` for data or `Flask` for the website).
*   `README.md`: The cover page of our project. It rapidly explains what the project is, what it looks like, and why it's important. 

---

## `app/` (The Web Portal)
This folder holds everything needed to power the website that HR executives will click on and interact with.

*   **`app.py`**: The Brain of the Website. 
    *   It wakes up the Flask web server.
    *   It links up your web browser to the actual Machine Learning models in the background.
    *   It securely checks your username and password when you log in.
    *   It accepts employee data, asks the AI model "will they quit?", and routes the answer back to your screen.
*   **`init_db.py`**: The Builder. If you run this file, it creates a blank, fresh database inside our project and inserts a default "admin" account so you can log into the website.
*   **`models.py`**: The Database Blueprint (Powered by SQLAlchemy). It explicitly defines what our data looks like when saved to the hard drive. It defines two things:
    1.  The `User` table (who is allowed to log in).
    2.  The `PredictionLog` table (a giant history book recording every time you run an AI prediction).

### `app/templates/` (The Visual Screens)
These are the HTML files that create the actual web pages you see.
*   `login.html`: The secure entry page demanding a username and password.
*   `index.html`: The main dashboard page asking if you want to analyze a single employee or upload a giant CSV spreadsheet.
*   `result.html`: Shows the risk of a *single* employee, complete with tailor-made advice on how to keep them.
*   `batch_result.html`: Displays a massive, scrollable table ranking hundreds of employees by their risk after a CSV upload.
*   `executive.html`: The beautiful, high-level screen with charts (like total risk distribution and department breakdowns) for the executives to stare at.
*   `executive_upload.html`: A tiny helper screen to drop the CSV file into the executive dashboard.
*   `history.html`: A table displaying past AI predictions saved securely in our SQLite database.

### `app/static/` (The Paintjob)
*   `style.css`: All the colors, animations, shadows, and fonts that make our website look extremely expensive and premium (using modern "glassmorphism" design).

---

## `src/` (The Data Science Engine)
This is the math powerhouse. These scripts train the AI BEFORE the website even launches.

*   **`data_preprocessing.py`**: The Cleaner. It takes raw, messy HR data, turns words into numbers (since AI only speaks math), and squishes all numbers to be on exactly the same scale (so a $10,000 salary doesn't overwhelm a 5-year tenure).
*   **`train_model.py`**: The Teacher (Baseline Model). It feeds our cleaned data into a `Logistic Regression` algorithm. It tests the algorithm until it reaches 88% accuracy, and then saves it to a file.
*   **`train_model_rf.py`**: The Advanced Teacher. It trains a more complex `Random Forest` algorithm capable of seeing hidden patterns and calculating exactly *which* factors (like Salary vs Boss) cause the most attrition.
*   **`evaluate_model.py`**: The Grader. It double checks the models' homework and prints out a "Report Card" detailing exact accuracies and errors.
*   **`retention_engine.py`**: The Strategist. A script that marries the predictions to actual English sentences (e.g. "Fix this employee's work-life balance!").
*   **`generate_fake_dataset.py`**: The Simulator. It generates a massive spreadsheet of 2,000 completely fake employees just so we have something to safely test our application with!

---

## `tests/` (The Automated QA Robots)
These files act as robot testers built using `pytest`. 
*   **`test_model.py`**: Checks that our trained AI brains (`.pkl` files) actually exist and work on the hard drive before we try to load them.
*   **`test_app.py`**: Checks that the website is alive. It literally pretends to be a user, clicks the login button, and makes sure the website responds correctly instead of crashing.

---

## `.github/workflows/` (The CI/CD Factory)
*   **`ci.yml`**: A set of remote commands. Every time you push Code to GitHub, this file tells GitHub to automatically boot up a Linux computer, install Python, and run the `tests/` folder to make absolutely sure you didn't break the project with your newest code.

---

## `data/` and `models/` (The Storage Lockers)
*   `data/employee_attrition.csv`: The Excel/CSV files filled with employee rows.
*   `models/attrition_model.pkl`: The saved "Brain" of our AI. By saving it here, the website doesn't need to re-learn everything every time it turns on.
*   `models/scaler.pkl`: The saved mathematical ruler that ensures all new data is properly squished before entering the brain. 
*   `models/rf_model.pkl`: The advanced Random Forest brain.

And that's everything! Every file works together in perfect harmony.
