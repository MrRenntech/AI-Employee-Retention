import os
import re

css_path = "app/static/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Precise variable overrides for :root
css = re.sub(
    r':root\s*\{.*?\n\}', 
    ''':root {
    --bg-color: #000000;      /* Pure Black */
    --card-bg: #050505;       /* Almost Black */
    --primary: #FFD700;       /* Lamborghini Yellow */
    --primary-hover: #CCAC00;
    --text-main: #FFFFFF;     /* White for readability */
    --text-muted: #666666;    /* Dark Grey */
    --border-color: #1a1a1a;  /* Very Dark Grey Border */
    --risk-high: #FFD700;     /* Yellow */
    --risk-low: #111111;      /* Barely visible dark */
}''', 
    css, 
    flags=re.DOTALL
)

# Precise variable overrides for [data-theme="light"]
css = re.sub(
    r'\[data-theme="light"\]\s*\{.*?\n\}', 
    '''[data-theme="light"] {
    --bg-color: #FFFFFF;      /* Pure White */
    --card-bg: #FFFFFF;       /* Pure White */
    --primary: #D5001C;       /* Porsche Red */
    --primary-hover: #AA0016;
    --text-main: #000000;     /* Black for readability */
    --text-muted: #888888;    /* Grey */
    --border-color: #DDDDDD;  /* Light Grey Border */
    --risk-high: #D5001C;     /* Red */
    --risk-low: #F5F5F5;      /* Off White */
}''', 
    css, 
    flags=re.DOTALL
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)


base_path = "app/templates/base.html"
with open(base_path, "r", encoding="utf-8") as f:
    base = f.read()

toggle_btn = """
                <div class="sidebar-link" onclick="toggleTheme()" style="cursor:pointer; margin-bottom: 20px; border: 1px solid var(--border-color); justify-content: center; border-radius: 4px;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    Toggle Theme Mode
                </div>
"""
if "toggleTheme()" not in base.split('<div class="sidebar-footer">')[1]:
    base = base.replace('<div class="sidebar-user">', toggle_btn + '<div class="sidebar-user">')
    with open(base_path, "w", encoding="utf-8") as f:
        f.write(base)


def convert_chart_colors(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    dynamic_chart_helper = """
    <script>
        const getCSSVar = (name, fallback) => {
            const val = getComputedStyle(document.documentElement).getPropertyValue(name);
            return val ? val.trim() : fallback;
        };
        const colPrimary = () => getCSSVar('--primary', '#FFD700');
        const colRiskLow = () => getCSSVar('--risk-low', '#111111');
        const colText = () => getCSSVar('--text-muted', '#555555');
"""
    # Simply replace the chart labels or hardcoded stuff.
    html = re.sub(r"backgroundColor:\s*\['[^']+',\s*'[^']+'\]", "backgroundColor: [colPrimary(), colRiskLow()]", html)
    html = re.sub(r"backgroundColor:\s*'[^']+'", "backgroundColor: colPrimary()", html)
    
    # Ensure helper is at the top of scripts
    if "const colPrimary = () =>" not in html and "Chart(" in html:
        html = html.replace("<script>\n    Chart.defaults", dynamic_chart_helper + "\n    Chart.defaults")
        html = html.replace("<script>\n    let simChart;", dynamic_chart_helper + "\n    let simChart;")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

convert_chart_colors("app/templates/dashboard.html")
convert_chart_colors("app/templates/executive.html")
convert_chart_colors("app/templates/simulator.html")

print("Fixed CSS overrides and injected missing toggle.")
