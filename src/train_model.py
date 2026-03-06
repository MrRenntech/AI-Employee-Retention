import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from data_preprocessing import load_and_preprocess

X, y, scaler, feature_names = load_and_preprocess(
    "data/employee_attrition.csv"
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Baseline Accuracy:", accuracy_score(y_test, preds))

joblib.dump(model, "models/attrition_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Baseline model saved.")
