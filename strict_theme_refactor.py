import os
import re

css_path = "app/static/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Force STRICT Dark/Yellow in :root
css = re.sub(r':root\s*\{.*?(?=\n\[data-theme="light"\])', '''
:root {
    --bg-color: #000000;      /* Pure Black */
    --card-bg: #030303;       /* Almost Black */
    --primary: #FFD700;       /* Lamborghini Yellow */
    --primary-hover: #CCAC00;
    --text-main: #FFFFFF;     /* White for readability */
    --text-muted: #555555;    /* Dark Grey */
    --border-color: #1a1a1a;  /* Very Dark Grey Border */
    --risk-high: #FFD700;     /* Yellow */
    --risk-low: #111111;      /* Barely visible dark */
}
''', css, flags=re.DOTALL)

# Force STRICT White/Red in [data-theme="light"]
css = re.sub(r'\[data-theme="light"\]\s*\{.*?\}', '''
[data-theme="light"] {
    --bg-color: #FFFFFF;      /* Pure White */
    --card-bg: #FFFFFF;       /* Pure White */
    --primary: #D5001C;       /* Porsche Red */
    --primary-hover: #9e0015;
    --text-main: #000000;     /* Black for readability */
    --text-muted: #888888;    /* Grey */
    --border-color: #DDDDDD;  /* Light Grey Border */
    --risk-high: #D5001C;     /* Red */
    --risk-low: #F5F5F5;      /* Off White */
}
''', css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)


def convert_chart_colors(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We want Chart.js scripts to pull colors dynamically.
    dynamic_chart_helper = """
    <script>
        const style = getComputedStyle(document.body);
        const colPrimary = () => style.getPropertyValue('--primary').trim() || '#FFD700';
        const colRiskLow = () => style.getPropertyValue('--risk-low').trim() || '#111111';
        const colText = () => style.getPropertyValue('--text-muted').trim() || '#555555';
"""
    # Simply replace the chart labels or hardcoded stuff.
    html = re.sub(r"backgroundColor:\s*\['[^']+',\s*'[^']+'\]", "backgroundColor: [colPrimary(), colRiskLow()]", html)
    html = re.sub(r"backgroundColor:\s*'[^']+'", "backgroundColor: colPrimary()", html)
    
    # Ensure helper is at the top of scripts
    if "const style = getComputedStyle" not in html and "Chart(" in html:
        html = html.replace("<script>\n    Chart.defaults", dynamic_chart_helper + "\n    Chart.defaults")
        html = html.replace("<script>\n    let simChart;", dynamic_chart_helper + "\n    let simChart;")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

convert_chart_colors("app/templates/dashboard.html")
convert_chart_colors("app/templates/executive.html")
convert_chart_colors("app/templates/simulator.html")

print("Strict colors applied")
