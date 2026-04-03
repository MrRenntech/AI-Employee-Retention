# The Ultimate Guide: How to Run This Project 🚀

This guide assumes you know nothing about programming. By following these steps exactly, you will turn your computer into an advanced AI server running the RetentionAI platform!

---

## Step 1: Prepare Your Computer
1. You must have **Python 3.8** (or higher) installed on your computer.
2. Open your terminal (Command Prompt for Windows, or Terminal for Mac).
3. Type this command to move perfectly into the project folder:
```bash
cd "e:\Projects\AI Employee\employee-attrition-ai"
```

## Step 2: Download the Tools (Libraries)
Your computer needs to download the math and website tools required to run the AI.
1. Run this command:
```bash
pip install -r requirements.txt
```
*(Wait until it finishes downloading things like Flask, Pandas, and Scikit-Learn).*

## Step 3: Initialize the Secure Database (First Time Only) 🔒
The website is securely locked so random people can't see HR files. We need to create a database and an Admin account.
1. Run this command:
```bash
python app/init_db.py
```
2. You will see a success message saying: "Default admin user created". 
   - **Your Username is:** `admin`
   - **Your Password is:** `password`

## Step 4: Boot up the Application! 🌐
Now we turn the engine on.
1. Run this command:
```bash
python app/app.py
```
2. The terminal will eventually say something like: `Running on http://127.0.0.1:5000`
3. **Open Google Chrome or Safari.**
4. In the address bar at the top, type exactly: `http://127.0.0.1:5000` and press Enter.

You are now looking at the login screen! Enter your admin/password credentials from Step 3, and enjoy the dashboard.

---

## (Optional) Advanced Data Science Steps

If you want to poke around the actual Machine Learning pipeline rather than just the website, here is how.

### Testing the Codebase (Quality Assurance)
Want to prove everything is working securely without crashing? We wrote robot testers!
```bash
python -m pytest tests/
```
This deploys invisible bots that test the login systems and the ML models, returning green passing marks if the code is healthy.

### Retraining the AI Brains (If you get new data)
If your company gets thousands of new employees next year, the AI needs to relearn the new patterns.
1. Ensure your new spreadsheet is at `data/employee_attrition.csv`.
2. Run the baseline training algorithm (this saves `attrition_model.pkl`):
```bash
python src/train_model.py
```
3. Run the advanced Random Forest algorithm (to recalculate what specific factors are driving people to quit the most):
```bash
python src/train_model_rf.py
```

### Automatic Text-Based Advice Engine
If you don't want to use the beautiful website, you can run an invisible text engineer that simply prints advice to the terminal:
```bash
python src/retention_engine.py
```
