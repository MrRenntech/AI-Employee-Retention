import joblib
from sklearn.metrics import classification_report, confusion_matrix
from data_preprocessing import load_and_preprocess

X, y, _, _ = load_and_preprocess("data/employee_attrition.csv")

model = joblib.load("models/attrition_model.pkl")

preds = model.predict(X)

print("Confusion Matrix:")
print(confusion_matrix(y, preds))

print("\nClassification Report:")
print(classification_report(y, preds))
