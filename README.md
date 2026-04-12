<div align="center">
  
# 🧠 Apex Analytics: HR Attrition Engine

[![Live Deployment](https://img.shields.io/badge/Live_Deployment-Up_%26_Running-success?style=for-the-badge&logo=render)](https://ai-employee-retention.onrender.com/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

**A Production-Ready AI Suite for Proactive HR Decision Making.**
</div>

---

## 🏗️ Architecture Flow

```mermaid
graph LR
    HR[HR Executive] -->|CSV Upload| UI[Dashboards UI]
    UI --> Flask[Flask REST API]
    Flask --> RF[Random Forest Alg]
    Flask --> LR[Logistic Regression]
    RF --> Insights[Deep Feature Analytics]
    LR --> Probability[Flight Risk Score]
    Probability & Insights --> UI
```

## 🌐 Live Application
👉 **[Access Apex Analytics Here](https://ai-employee-retention.onrender.com/)**
