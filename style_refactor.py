import os
import re

css_path = "app/static/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Change variables
css = re.sub(r'--bg-color:.*?;', '--bg-color: #050505;', css)
css = re.sub(r'--card-bg:.*?;', '--card-bg: #111111;', css)
# Giallo Yellow
css = re.sub(r'--primary:.*?;', '--primary: #FFD700;', css)
css = re.sub(r'--primary-hover:.*?;', '--primary-hover: #E5C100;', css)
# Keeping text main and muted as is, keeping risk high as red
# But let's change risk-low from bright green to a sleek silver since it's luxury
css = re.sub(r'--risk-low:.*?;', '--risk-low: #A0AAB5;', css)
css = re.sub(r'--border-color:.*?;', '--border-color: #222222;', css)

# Make borders sharp: Replace border-radius: \d+px with 0 or 2px
css = re.sub(r'border-radius:\s*12px;', 'border-radius: 0;', css)
css = re.sub(r'border-radius:\s*8px;', 'border-radius: 2px;', css)
css = re.sub(r'border-radius:\s*10px;', 'border-radius: 2px;', css)
css = re.sub(r'border-radius:\s*6px;', 'border-radius: 0;', css)

# Force font to have some tracking for that luxury feel
css = re.sub(r'body\s*{.*?font-family:.*?}', r'body { font-family: "Inter", sans-serif; letter-spacing: 0.5px; }', css, flags=re.DOTALL)

# Let's add text-transform uppercase to headings
css += "\nh1, h2, h3, h4, th { text-transform: uppercase; letter-spacing: 2px; font-weight: 700; }\n"
css += "\n.dashboard-grid .kpi-card { border-left: 3px solid var(--primary); }\n"
css += "\n.main-content { background-image: radial-gradient(circle at 50% 0%, rgba(255, 215, 0, 0.03) 0%, transparent 60%); }\n"

# In dashboard.html there's hardcoded chart colors. 
dash_html = "app/templates/dashboard.html"
with open(dash_html, "r", encoding="utf-8") as f:
    dash_c = f.read()

dash_c = dash_c.replace("#06b6d4", "#FFD700")
dash_c = dash_c.replace("rgba(6, 182, 212,", "rgba(255, 215, 0,")

with open(dash_html, "w", encoding="utf-8") as f:
    f.write(dash_c)

# Executive hardcoded chart colors
exec_html = "app/templates/executive.html"
if os.path.exists(exec_html):
    with open(exec_html, "r", encoding="utf-8") as f:
        exec_c = f.read()
    exec_c = exec_c.replace("#06b6d4", "#FFD700")
    exec_c = exec_c.replace("rgba(6, 182, 212,", "rgba(255, 215, 0,")
    with open(exec_html, "w", encoding="utf-8") as f:
        f.write(exec_c)

# Result HTML chart colors
res_html = "app/templates/result.html"
if os.path.exists(res_html):
    with open(res_html, "r", encoding="utf-8") as f:
        res_c = f.read()
    res_c = res_c.replace("#06b6d4", "#FFD700")
    res_c = res_c.replace("rgba(6, 182, 212,", "rgba(255, 215, 0,")
    with open(res_html, "w", encoding="utf-8") as f:
        f.write(res_c)

# base HTML hardcoded sidebar active pill
base_html = "app/templates/base.html"
if os.path.exists(base_html):
    with open(base_html, "r", encoding="utf-8") as f:
        bc_c = f.read()
    bc_c = bc_c.replace("rgba(6, 182, 212,", "rgba(255, 215, 0,")
    with open(base_html, "w", encoding="utf-8") as f:
        f.write(bc_c)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Style redesign complete")
