# 02_water_quality_report.py

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Add current folder to Python path
# -----------------------------
sys.path.append(os.getcwd())

# -----------------------------
# Import load function
# -----------------------------
from inspect_water_quality import load_water_data

# -----------------------------
# 1️⃣ Load cleaned data
# -----------------------------
file_path = r"C:\Users\HP\water_quality\Water_pond_tanks_2021.csv"
df = load_water_data(file_path)
if df is None:
    exit("Failed to load data.")

# -----------------------------
# 2️⃣ Define safe ranges and educational guidance
# -----------------------------
safe_ranges = {
    'Temperature': (0, 35),
    'Dissolved Oxygen (mg/L)': (5, 14),
    'pH': (6.5, 8.5),
    'Conductivity (?mhos/cm)': (0, 1000),
    'BOD (mg/L)': (0, 5),
    'Nitrate N + Nitrite N(mg/L)': (0, 10),
    'Fecal Coliform (MPN/100ml)': (0, 100),
    'Total Coliform (MPN/100ml)': (0, 500)
}

edu_guidance = {
    'Temperature': "Avoid extremely hot/cold water; store safely.",
    'Dissolved Oxygen (mg/L)': "Low DO may indicate pollution; treat before drinking.",
    'pH': "Extreme pH can harm health; neutralize water before use.",
    'Conductivity (?mhos/cm)': "High salts; use filtration before drinking.",
    'BOD (mg/L)': "High BOD indicates pollution; avoid drinking.",
    'Nitrate N + Nitrite N(mg/L)': "High nitrates dangerous; filter or RO before use.",
    'Fecal Coliform (MPN/100ml)': "Indicates bacteria; boil water before drinking.",
    'Total Coliform (MPN/100ml)': "High contamination; avoid drinking directly."
}

risk_colors = {'Low': 'green', 'Moderate': 'yellow', 'High': 'red'}

# -----------------------------
# 3️⃣ Compute Risk Levels
# -----------------------------
for param, (low, high) in safe_ranges.items():
    # Find Min/Max columns
    min_col = [col for col in df.columns if param in col and "Min" in col][0]
    max_col = [col for col in df.columns if param in col and "Max" in col][0]

    df[param + ' Risk'] = df.apply(
        lambda row: 'High' if row[min_col] < low or row[max_col] > 2*high
                    else 'Moderate' if row[min_col] < low or row[max_col] > high
                    else 'Low',
        axis=1
    )

# -----------------------------
# 4️⃣ Alerts Report
# -----------------------------
print("\n=== Water Quality Alerts Report ===")
for param in safe_ranges.keys():
    high_count = (df[param + ' Risk'] == 'High').sum()
    mod_count = (df[param + ' Risk'] == 'Moderate').sum()
    print(f"{param}: High={high_count}, Moderate={mod_count}, Guidance: {edu_guidance[param]}")

# -----------------------------
# 5️⃣ Visualizations (Red/Yellow/Green)
# -----------------------------
for param in safe_ranges.keys():
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x=param + ' Risk', palette=risk_colors)
    plt.title(f"{param} Risk Levels")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Locations")
    plt.show()

# -----------------------------
# 6️⃣ Save Processed Report
# -----------------------------
output_path = r"C:\Users\HP\water_quality\processed_water_report_colored.csv"
df.to_csv(output_path, index=False)
print(f"\nProcessed water report saved successfully at:\n{output_path}")
