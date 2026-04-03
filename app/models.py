from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    employee_id = db.Column(db.String(50), nullable=True) # Optional for batch mode
    prediction_type = db.Column(db.String(20), nullable=False) # 'Individual' or 'Batch'
    probability = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(50), nullable=False)
    # Storing input features as a JSON string or simplified
    details = db.Column(db.Text, nullable=True) 
