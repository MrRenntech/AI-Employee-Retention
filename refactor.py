import os
import re

templates_dir = "app/templates"
files_to_update = ["predict.html", "executive.html", "executive_upload.html", "history.html", "batch_result.html", "result.html"]

for f in files_to_update:
    path = os.path.join(templates_dir, f)
    if not os.path.exists(path):
        print(f"Skipping {f}, not found.")
        continue
        
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check if already extended
    if "{% extends" in content:
        continue
        
    # Remove everything before </nav> including </nav>
    if "<nav" in content and "</nav>" in content:
        content = re.sub(r'(?s).*?</nav>', '', content, count=1)
    else:
        # Just remove doctype, head, body
        content = re.sub(r'(?s).*?<body>', '', content, count=1)
        
    # Remove </body></html>
    content = re.sub(r'(?s)</body>.*', '', content)
    
    new_content = "{% extends 'base.html' %}\n\n{% block content %}\n" + content.strip() + "\n{% endblock %}\n"
    
    with open(path, "w", encoding="utf-8") as file:
        file.write(new_content)
        
print("Templates reformatted to block inheritance.")
