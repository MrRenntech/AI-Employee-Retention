import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import load_and_preprocess

# Load and preprocess data
X, y, scaler, feature_names = load_and_preprocess("data/ibm_dataset.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print(f"Random Forest Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, preds))

# Save Model
joblib.dump(model, "models/rf_model.pkl")
print("Random Forest model saved to models/rf_model.pkl")

# Feature Importance
importances = model.feature_importances_
feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False).head(10)

print("\nTop 10 Important Features:")
print(feature_imp_df)

# Save Feature Importance Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_imp_df, palette='viridis')
plt.title('Top 10 Factors Contributing to Attrition')
plt.tight_layout()
plt.savefig('models/feature_importance.png')
print("Feature importance plot saved to models/feature_importance.png")
