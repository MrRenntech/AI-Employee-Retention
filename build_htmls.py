import os

about_html = """{% extends 'base.html' %}
{% block content %}
<div class="dashboard-container">
    <div style="max-width: 800px; margin: 0 auto; color: var(--text-main);">
        <h1 style="color: var(--primary); font-size: 32px; border-bottom: 2px solid var(--border-color); padding-bottom: 10px; margin-bottom: 30px;">Architecture & Purpose</h1>
        
        <div class="card" style="margin-bottom: 25px;">
            <h2 style="font-size: 20px; margin-bottom: 15px; color: var(--text-main);">The Apex Mission</h2>
            <p style="color: var(--text-muted); line-height: 1.6;">Apex Analytics is an enterprise-grade artificial intelligence engine designed specifically to intercept and neutralize employee attrition before it occurs. By ingesting over 23 distinct workforce features—ranging from commute vectors to compensation matrix anomalies—our engine acts as an early warning radar for HR executives.</p>
        </div>

        <div class="card" style="margin-bottom: 25px;">
            <h2 style="font-size: 20px; margin-bottom: 15px; color: var(--text-main);">Under The Hood: Model Architecture</h2>
            <p style="color: var(--text-muted); line-height: 1.6;">The analytics core runs purely on <strong>Scikit-Learn Logistic Regression</strong> and <strong>Random Forest Ensembles</strong>, scaled dynamically via StandardScaler architecture. The probability matrix operates on a strict 0.0 to 100.0 output, allowing definitive "High Risk" flags at a 60% probability threshold.</p>
            <ul style="color: var(--text-muted); line-height: 1.8; margin-top: 10px; padding-left: 20px;">
                <li><strong>Dimensionality:</strong> 23 Vector Features</li>
                <li><strong>Scaling:</strong> Active Z-Score Normalization</li>
                <li><strong>Engine:</strong> Multi-Class Classification</li>
            </ul>
        </div>
        
        <div class="card">
            <h2 style="font-size: 20px; margin-bottom: 15px; color: var(--text-main);">Theme Engine</h2>
            <p style="color: var(--text-muted); line-height: 1.6;">Apex Analytics features a dual-theme interface designed specifically for high-performance aesthetics: <strong>Lamborghini Giallo</strong> (Dark Mode) and <strong>Porsche Carmine Red</strong> (Light Mode). Toggle between them seamlessly using the switch in your command sidebar.</p>
        </div>
    </div>
</div>
{% endblock %}
"""

batch_html = """{% extends 'base.html' %}
{% block content %}
<div class="dashboard-container" style="max-width: 600px; margin: 0 auto;">
    <h2 style="color: var(--primary); font-size: 24px; margin-bottom: 10px;">Bulk Roster Inference</h2>
    <p style="color: var(--text-muted); font-size: 14px; margin-bottom: 30px;">Upload an organization-wide CSV snapshot to instantly process thousands of attrition probabilities.</p>
    
    <div class="card" style="text-align: center; padding: 50px 20px; border: 2px dashed var(--border-color);">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--primary)" stroke-width="2" style="margin-bottom: 20px;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
        <form action="{{ url_for('batch_processing') }}" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required style="margin-bottom: 20px; color: var(--text-main); font-family: Inter;">
            <br>
            <button type="submit" class="btn" style="background: var(--primary); color: #000; font-weight: bold; border: none; padding: 12px 30px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px;">Deploy Analysis</button>
        </form>
    </div>
</div>
{% endblock %}
"""

batch_result_html = """{% extends 'base.html' %}
{% block content %}
<div class="dashboard-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <h2 style="color: var(--primary); font-size: 24px;">Batch Inference Results</h2>
        <a href="{{ url_for('batch_processing') }}" class="btn" style="color: var(--primary); text-decoration: none; font-size: 14px; text-transform: uppercase;">&larr; Run New Batch</a>
    </div>
    
    <div class="card data-table-container">
        {{ tables[0]|safe }}
    </div>
</div>
<style>
    table.data { width: 100%; border-collapse: collapse; }
    table.data th { background: rgba(0,0,0,0.1) !important; color: var(--primary) !important; text-align: left; padding: 12px; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;}
    table.data td { padding: 12px; color: var(--text-main); border-bottom: 1px solid var(--border-color); font-size: 14px;}
</style>
{% endblock %}
"""

simulator_html = """{% extends 'base.html' %}
{% block content %}
<div class="dashboard-container">
    <h2 style="color: var(--primary); font-size: 24px; margin-bottom: 10px;">Tactical Attrition Simulator</h2>
    <p style="color: var(--text-muted); font-size: 14px; margin-bottom: 30px;">Dynamically adjust employee metrics to model "What-If" retention strategies in real-time.</p>
    
    <div class="grid" style="display: grid; grid-template-columns: 1fr 300px; gap: 30px; align-items: start;">
        <div class="card" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-height: 70vh; overflow-y: auto;">
            {% for name in FEATURE_NAMES %}
            <div style="display: flex; flex-direction: column; gap: 5px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <label style="color: var(--text-main); font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px;">{{ name }}</label>
                    <span id="val_{{ name }}" style="color: var(--primary); font-weight: bold; font-size: 12px;">0</span>
                </div>
                <input type="range" class="sim-slider" id="feat_{{ name }}" name="{{ name }}" min="0" max="100000" value="0" oninput="updateVal('{{ name }}'); triggerSim();" style="width: 100%; accent-color: var(--primary);">
            </div>
            {% endfor %}
        </div>
        
        <div class="card" style="text-align: center; position: sticky; top: 100px;">
            <p style="font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 2px;">Real-Time Probability</p>
            <div id="gauge-container" style="position: relative; width: 100%; height: 200px; display: flex; justify-content: center; align-items: center; margin-top: 20px;">
                <canvas id="simGauge"></canvas>
                <div style="position: absolute; display: flex; flex-direction: column; align-items: center;">
                    <span id="probPercent" style="font-size: 40px; font-weight: bold; color: var(--text-main);">0%</span>
                    <span id="riskLabel" style="font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: var(--risk-low);">Low Risk</span>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    let simChart;
    
    function updateVal(name) {
        document.getElementById('val_' + name).innerText = document.getElementById('feat_' + name).value;
    }
    
    // Set sensible defaults
    document.addEventListener('DOMContentLoaded', () => {
        // Init chart
        simChart = new Chart(document.getElementById('simGauge'), {
            type: 'doughnut',
            data: {
                labels: ['Risk', 'Safe'],
                datasets: [{
                    data: [0, 100],
                    backgroundColor: [getComputedStyle(document.documentElement).getPropertyValue('--risk-high').trim(), '#e2e8f0'],
                    borderWidth: 0,
                    circumference: 180,
                    rotation: 270,
                    cutout: '80%'
                }]
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: { legend: { display: false }, tooltip: { enabled: false } }
            }
        });
        
        // Mock data initialization just so sliders aren't 0
        const defaults = {'Age': 35, 'DailyRate': 800, 'DistanceFromHome': 10, 'Education': 3, 'EnvironmentSatisfaction': 3, 'HourlyRate': 65, 'JobInvolvement': 3, 'JobLevel': 2, 'JobSatisfaction': 3, 'MonthlyIncome': 6000, 'MonthlyRate': 15000, 'NumCompaniesWorked': 3, 'PercentSalaryHike': 15, 'PerformanceRating': 3, 'RelationshipSatisfaction': 3, 'StockOptionLevel': 1, 'TotalWorkingYears': 10, 'TrainingTimesLastYear': 3, 'WorkLifeBalance': 3, 'YearsAtCompany': 7, 'YearsInCurrentRole': 4, 'YearsSinceLastPromotion': 2, 'YearsWithCurrManager': 4};
        
        for (let key in defaults) {
            let el = document.getElementById('feat_' + key);
            if(el) {
                if (key.includes('Income') || key.includes('Rate')) { el.max = 20000; }
                else if (key.includes('Years') || key === 'Age') { el.max = 60; }
                else if (key.includes('Satisfaction') || key.includes('Level') || key.includes('Balance')) { el.max = 4; }
                
                el.value = defaults[key];
                updateVal(key);
            }
        }
        triggerSim();
    });
    
    let debounceTimer;
    function triggerSim() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            const payload = {};
            document.querySelectorAll('.sim-slider').forEach(el => payload[el.name] = el.value);
            
            fetch('/simulate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            }).then(r => r.json()).then(data => {
                if(data.new_probability !== undefined) {
                    const prob = parseFloat(data.new_probability);
                    document.getElementById('probPercent').innerText = prob.toFixed(1) + "%";
                    
                    const isHighRisk = prob >= 60;
                    document.getElementById('riskLabel').innerText = isHighRisk ? "High Risk" : "Low Risk";
                    document.getElementById('riskLabel').style.color = isHighRisk ? 'var(--risk-high)' : 'var(--risk-low)';
                    
                    simChart.data.datasets[0].data = [prob, 100 - prob];
                    simChart.data.datasets[0].backgroundColor[0] = isHighRisk ? 
                        getComputedStyle(document.documentElement).getPropertyValue('--risk-high').trim() : 
                        getComputedStyle(document.documentElement).getPropertyValue('--risk-low').trim();
                        
                    simChart.update();
                }
            });
        }, 300);
    }
</script>
{% endblock %}
"""

with open("app/templates/about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
with open("app/templates/batch.html", "w", encoding="utf-8") as f:
    f.write(batch_html)
with open("app/templates/batch_result.html", "w", encoding="utf-8") as f:
    f.write(batch_result_html)
with open("app/templates/simulator.html", "w", encoding="utf-8") as f:
    f.write(simulator_html)

print("Generated new feature HTML files.")
