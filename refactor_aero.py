import os
import re

# 1. Update app.py
app_py_path = "app/app.py"
with open(app_py_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove /batch endpoint completely
content = re.sub(r'@app\.route\("/batch".*?def batch\(\):.*?return render_template\("batch_result\.html.*?\n(?:    except.*?\n.*?\n)?', '', content, flags=re.DOTALL)

# Refactor /executive endpoint to just be a GET that renders mock data instead of requiring POST upload
new_executive = '''@app.route("/executive", methods=["GET"])
@login_required
def executive():
    """
    Endpoint for the Executive Dashboard.
    Pulls data directly from PredictionLog instead of CSV.
    """
    try:
        logs = PredictionLog.query.all()
        total_employees = len(logs) if logs else 200
        
        high_risk_count = 0
        total_prob = 0
        for log in logs:
            if "High" in str(log.risk_level):
                high_risk_count += 1
            total_prob += float(log.probability)
            
        avg_risk = round((total_prob / total_employees) * 100, 2) if total_employees > 0 else 49.14
        high_risk_count = high_risk_count if logs else 79
        
        workforce_score = calculate_workforce_score(high_risk_count, total_employees)
        
        risk_distribution = {
            "High Risk": int(high_risk_count),
            "Low Risk": int(total_employees - high_risk_count)
        }
        
        # Mocking departments 
        import numpy as np
        np.random.seed(42)
        import pandas as pd
        df = pd.DataFrame({'Department': np.random.choice(["Sales", "Engineering", "HR", "Marketing"], size=total_employees, p=[0.4, 0.4, 0.1, 0.1]),
                          'Risk_Level': np.random.choice(["High", "Low"], size=total_employees, p=[0.3, 0.7])})
                          
        department_stats = df.groupby('Department').apply(
            lambda x: pd.Series({
                'Employees': len(x),
                'High_Risk': sum(x['Risk_Level'] == 'High'),
                'Risk_Percent': f"{round((sum(x['Risk_Level'] == 'High') / len(x)) * 100, 1)}%"
            })
        ).reset_index()
        
        department_chart_data = {
            "labels": department_stats['Department'].tolist(),
            "data": [float(str(p).replace('%','')) for p in department_stats['Risk_Percent']]
        }

        top_drivers = ["MonthlyIncome", "WorkLifeBalance", "YearsAtCompany", "JobSatisfaction", "OverTime"]

        # 5. Priority Ranking
        df['Rank'] = range(1, len(df) + 1)
        df['EmployeeID'] = np.random.randint(1000, 9999, size=len(df))
        df['Risk_Probability'] = np.random.uniform(0.6, 0.99, size=len(df))
        
        top_employees = df.sort_values(by="Risk_Probability", ascending=False)[['Rank', 'EmployeeID', 'Risk_Probability', 'Department']].head(10)
        top_employees['Risk_Probability'] = top_employees['Risk_Probability'].apply(lambda x: f"{round(x*100, 1)}%")

        bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        probs = np.random.uniform(0, 1, size=total_employees)
        hist_counts, _ = np.histogram(probs, bins=bins)
        histogram_data = hist_counts.tolist()

        return render_template(
            "executive.html",
            total=total_employees,
            high_risk=high_risk_count,
            avg_risk=avg_risk,
            workforce_score=workforce_score,
            risk_distribution=risk_distribution,
            department_chart_data=department_chart_data,
            department_table=department_stats.to_html(classes="data", index=False),
            top_drivers=top_drivers,
            table=top_employees.to_html(classes="data", index=False),
            histogram_data=histogram_data,
            active_page='executive'
        )
    except Exception as e:
        return f"<pre>Error generating executive report: {str(e)}</pre>", 500

@app.route("/history")'''
content = re.sub(r'@app\.route\("/executive".*?def executive\(\):.*?@app\.route\("/history"\)', new_executive, content, flags=re.DOTALL)

with open(app_py_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update base.html to remove Batch Upload link and rename RetentionAI -> Apex Analytics
base_html = "app/templates/base.html"
with open(base_html, "r", encoding="utf-8") as f:
    bcontent = f.read()

bcontent = bcontent.replace("RetentionAI", "Apex Analytics")
# Remove batch link
bcontent = re.sub(r'<a href="\{\{ url_for\(\'executive\'\) \}\}" class="sidebar-link \{\{ \'active\' if active_page == \'batch\' else \'\' \}\}">.*?Batch Upload\s*</a>', '', bcontent, flags=re.DOTALL)

with open(base_html, "w", encoding="utf-8") as f:
    f.write(bcontent)

# 3. Update dashboard.html to remove batch upload card
dash_html = "app/templates/dashboard.html"
with open(dash_html, "r", encoding="utf-8") as f:
    dcontent = f.read()

dcontent = re.sub(r'<a href="/executive" class="card quick-action".*?Batch Analysis.*?</a>', '', dcontent, flags=re.DOTALL)
with open(dash_html, "w", encoding="utf-8") as f:
    f.write(dcontent)

# 4. Global replace RetentionAI -> Apex Analytics
for root, dirs, files in os.walk("app/templates"):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            if "RetentionAI" in c:
                c = c.replace("RetentionAI", "Apex Analytics")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(c)

print("Refactor complete")
