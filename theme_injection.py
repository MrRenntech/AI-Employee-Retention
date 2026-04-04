import os
import re

# 1. Update style.css
css_path = "app/static/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

light_theme = """
/* Dual Theme Engine */
[data-theme="light"] {
    --bg-color: #f3f4f6;       /* Chalk White */
    --card-bg: #ffffff;        /* Pure White */
    --primary: #D5001C;        /* Porsche Carmine Red */
    --primary-hover: #b30017;
    --text-main: #111827;      /* Stark Black */
    --text-muted: #6b7280;     /* Grey */
    --border-color: #e5e7eb;   /* Light metallic silver */
    --risk-high: #D5001C;      /* Porsche Red */
    --risk-low: #10b981;       /* Retain standard green for light mode */
}

/* Force Light Theme Adjustments */
[data-theme="light"] .sidebar {
    background: #ffffff;
    box-shadow: 1px 0 10px rgba(0,0,0,0.05);
}
[data-theme="light"] .kpi-card, [data-theme="light"] .card {
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}
[data-theme="light"] table.data th {
    background: #f8fafc !important;
}
[data-theme="light"] .main-content {
    background-image: none !important;
}
"""

if "[data-theme=\"light\"]" not in css:
    css += "\n" + light_theme
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)

# 2. Update base.html to add Theme Switch script and Sidebar links
base_html = "app/templates/base.html"
with open(base_html, "r", encoding="utf-8") as f:
    base = f.read()

# Add script to head to load theme
theme_script = """
    <script>
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
        
        function toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            const target = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', target);
            localStorage.setItem('theme', target);
            // Optionally reload chart.js defaults
            window.location.reload(); 
        }
    </script>
"""
if "toggleTheme()" not in base:
    base = base.replace('</head>', theme_script + '</head>')

# Add new nav links
nav_addition = """
                <a href="{{ url_for('simulator') }}" class="sidebar-link {{ 'active' if active_page == 'simulator' else '' }}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                    Simulation Engine
                </a>
                <a href="{{ url_for('batch_processing') }}" class="sidebar-link {{ 'active' if active_page == 'batch_proc' else '' }}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                    Batch Processing
                </a>
                <a href="{{ url_for('about') }}" class="sidebar-link {{ 'active' if active_page == 'about' else '' }}">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
                    About AI Core
                </a>
"""
# inject nav addition before closing </nav>
if "Simulation Engine" not in base:
    base = base.replace('</nav>', nav_addition + '</nav>')

# Add theme switch button
footer_addition = """
                <div class="sidebar-link" onclick="toggleTheme()" style="cursor:pointer; margin-bottom: 10px; border: 1px solid var(--border-color); justify-content: center;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    Toggle Theme
                </div>
"""
if "toggleTheme()" not in base:
    # already checked above but checking footer specifically
    base = base.replace('<div class="sidebar-user">', footer_addition + '<div class="sidebar-user">')

with open(base_html, "w", encoding="utf-8") as f:
    f.write(base.replace('<html lang="en">', '<html lang="en" data-theme="dark">'))

# 3. Modify app.py
app_path = "app/app.py"
with open(app_path, "r", encoding="utf-8") as f:
    app_py = f.read()

new_routes = """
@app.route("/simulator")
@login_required
def simulator():
    return render_template("simulator.html", active_page='simulator', FEATURE_NAMES=FEATURE_NAMES)

@app.route("/about")
@login_required
def about():
    return render_template("about.html", active_page='about')

@app.route("/batch_processing", methods=["GET", "POST"])
@login_required
def batch_processing():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files["file"]
        if file.filename == '':
            return "No selected file", 400
            
        try:
            df = pd.read_csv(file)
            missing_cols = [col for col in FEATURE_NAMES if col not in df.columns]
            if missing_cols:
                return f"Missing columns in CSV: {', '.join(missing_cols)}", 400

            df_scaled = scaler.transform(df[FEATURE_NAMES])
            probs = attrition_model.predict_proba(df_scaled)[:,1]
            df["Attrition Risk"] = [f"{round(p*100, 1)}%" for p in probs]
            df["Risk Tag"] = ["High Risk" if p>=0.6 else "Low Risk" for p in probs]
            
            df['RawProb'] = probs
            df = df.sort_values(by="RawProb", ascending=False).drop(columns=['RawProb'])

            save_prediction_log("BATCH_UI", "Batch Processing", float(np.mean(probs)), "Mixed", {"rows": len(df)})
            
            return render_template("batch_result.html", active_page='batch_proc', tables=[df.to_html(classes='data', index=False)])
        except Exception as e:
            return f"Error: {e}", 500
            
    return render_template("batch.html", active_page='batch_proc')
"""

if "@app.route(\"/simulator\")" not in app_py:
    app_py = app_py.replace('if __name__ == "__main__":', new_routes + '\nif __name__ == "__main__":')
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_py)

print("Infrastructure scaffolded successfully.")
