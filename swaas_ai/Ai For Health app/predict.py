import pickle
import pandas as pd

# Load model
with open("health_model.pkl", "rb") as f:
    model = pickle.load(f)

# Patient symptoms
patient = {"fever": 1, "cough": 0, "fatigue": 1, "headache": 1}

# Convert to DataFrame with same feature names
patient_df = pd.DataFrame([patient])

prediction = model.predict(patient_df)

print(f"Predicted disease: {prediction[0]}")
