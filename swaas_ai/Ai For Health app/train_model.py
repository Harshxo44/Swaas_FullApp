# train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# -----------------------------
# 1️⃣ Load dataset
# -----------------------------
file_path = r"C:\Users\HP\water_quality\Water_pond_tanks_2021.csv"
df = pd.read_csv(file_path, encoding='cp1252')

# -----------------------------
# 2️⃣ Clean data
# -----------------------------
# Replace "-" or invalid strings with NaN
df.replace("-", np.nan, inplace=True)

# Convert numeric columns to float
numeric_cols = [
    'Temperature\n?C (Min)', 'Temperature\n?C (Max)',
    'Dissolved Oxygen (mg/L) (Min)', 'Dissolved Oxygen (mg/L) (Max)',
    'pH (Min)', 'pH (Max)',
    'Conductivity (?mhos/cm) (Min)', 'Conductivity (?mhos/cm) (Max)',
    'BOD (mg/L) (Min)', 'BOD (mg/L) (Max)',
    'Nitrate N + Nitrite N(mg/L) (Min)', 'Nitrate N + Nitrite N(mg/L) (Max)',
    'Fecal Coliform (MPN/100ml) (Min)', 'Fecal Coliform (MPN/100ml) (Max)',
    'Total Coliform (MPN/100ml) (Min)', 'Total Coliform (MPN/100ml) (Max)'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values
df.dropna(inplace=True)

# -----------------------------
# 3️⃣ Create target variable
# -----------------------------
# Example thresholds (same as risk report)
def risk_level(row):
    if (row['BOD (mg/L) (Max)'] > 6) or (row['Fecal Coliform (MPN/100ml) (Max)'] > 500):
        return "High"
    elif (row['BOD (mg/L) (Max)'] > 3) or (row['Fecal Coliform (MPN/100ml) (Max)'] > 200):
        return "Moderate"
    else:
        return "Low"

df['Risk'] = df.apply(risk_level, axis=1)

# Encode target
le = LabelEncoder()
df['Risk_encoded'] = le.fit_transform(df['Risk'])

# -----------------------------
# 4️⃣ Prepare features and target
# -----------------------------
X = df[numeric_cols]
y = df['Risk_encoded']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 5️⃣ Split train/test
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6️⃣ Train Random Forest
# -----------------------------
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# -----------------------------
# 7️⃣ Evaluate
# -----------------------------
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# -----------------------------
# 8️⃣ Save model and scaler
# -----------------------------
model_path = "water_quality_risk_model.pkl"
joblib.dump({'model': clf, 'scaler': scaler, 'label_encoder': le}, model_path)
print(f"Trained model saved at: {model_path}")
