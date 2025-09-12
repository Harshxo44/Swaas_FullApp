# 01_inspect_water_quality.py

import pandas as pd
import numpy as np

def load_water_data(file_path):
    """
    Load and clean water quality dataset (CSV or Excel).
    Returns cleaned DataFrame.
    """
    try:
        if file_path.endswith('.csv'):
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(file_path, encoding='cp1252')
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type")

        # Identify numerical columns (replace '-' with NaN)
        numerical_cols = [col for col in df.columns if any(x in col for x in [
            'Temperature', 'Dissolved Oxygen', 'pH', 'Conductivity', 
            'BOD', 'Nitrate', 'Coliform'])]

        df[numerical_cols] = df[numerical_cols].replace('-', np.nan)
        df[numerical_cols] = df[numerical_cols].apply(pd.to_numeric, errors='coerce')
        df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

        return df

    except Exception as e:
        print("Error loading data:", e)
        return None

# Optional: for standalone testing
if __name__ == "__main__":
    file_path = r"C:\Users\HP\water_quality\Water_pond_tanks_2021.csv"
    df = load_water_data(file_path)
    if df is not None:
        print("Data loaded successfully! Shape:", df.shape)
