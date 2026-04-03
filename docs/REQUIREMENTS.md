# Project Requirements & Dependencies 🛠️

To make this project run, Python borrows tools built by smart people across the world. Instead of reinventing the wheel, we install these toolkits (libraries). 

This file explains exactly what tools we use, and *why* a total beginner would care about them. The system runs flawlessly on **Python 3.8 or higher.**

---

## 1. The Web Toolkit (How the website survives)
These tools turn basic Python code into a beautiful, interactive website that works in a browser (like Chrome or Safari).

*   **Flask**: The core skeleton of our entire website. It's an invisible engine that listens to your web browser and responds by handing it HTML pages.
*   **Flask-Login**: This is our bouncer. It stands at the door, creates "sessions" (meaning the website remembers you logged in 5 minutes ago), and violently ejects anyone trying to access the `/predict` links if they aren't logged in.
*   **Flask-SQLAlchemy**: This handles talking to our database. Instead of writing extremely complex SQL commands (like `SELECT * FROM table JOIN other_table`), this tool lets us just type `User.query.all()` in Python, and it translates that into database queries automatically.
*   **Werkzeug**: This is the ultimate security guard for passwords. When we create our `admin:password` account, Werkzeug encrypts that password into unrecognizable scrambled text using `pbkdf2:sha256` hashing so hackers can't read it.

## 2. Core Data Science (The Number Crunchers)
These tools act as the spreadsheet engine for Python.

*   **pandas**: Imagine Microsoft Excel, but built for code. Pandas lets us ingest a CSV file containing 2,000 employee rows, slice out columns in a fraction of a millisecond, sort them, and format them back into tables.
*   **numpy**: A high-speed mathematical engine. AI calculates thousands of data vectors simultaneously. Standard Python loops would take hours; Numpy does it instantly.

## 3. The Artificial Intelligence (The Brains)
*   **scikit-learn**: This is the absolute titan of Machine Learning. It houses the algorithms we used:
    *   `Logistic Regression`: A math formula we used as our baseline AI.
    *   `LabelEncoder`: Changes text like "Sales Dept" into numbers like `0`, because AI only understands math.
    *   `StandardScaler`: Our equalizer. It makes sure that a feature like "Monthly Income" (e.g. 5000) doesn't completely overwhelm "Years at Company" (e.g. 5) by transforming them to an identical statistical scale.
*   **joblib**: The "Save Game" button. After we spend time training the AI to be 88% accurate, `joblib` allows us to save that giant brain state into a `.pkl` file on the hard drive. We just 'load' the save file the next time we boot the website!

## 4. Visualization & Testing
*   **matplotlib** & **seaborn**: These tools take massive blocks of numbers and draw beautiful, readable line charts and bar graphs (useful for notebooks and backend analysis).
*   **pytest**: A toolkit for building robot testers. Instead of manually clicking the website a hundred times to test if it works, `pytest` runs an invisible browser, simulates logging in, and asserts whether the site is running perfectly or broken.

---

## Automatic Installation
You can magically download all these tools onto your computer in 10 seconds by opening your console and running:
```bash
pip install -r requirements.txt
```
