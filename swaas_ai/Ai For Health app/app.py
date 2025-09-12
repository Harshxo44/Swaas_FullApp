# app.py
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import joblib
import pandas as pd

# -----------------------------
# Initialize app and load model
# -----------------------------
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load trained model, scaler, and label encoder
model_data = joblib.load("water_quality_risk_model.pkl")
model = model_data['model']
scaler = model_data['scaler']
le = model_data['label_encoder']

# Numeric columns expected by the model
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


# Guidance messages
guidance_dict = {
    "Low": "Water is safe. Normal precautions recommended.",
    "Moderate": "Caution! Boil water or use filtration before consumption.",
    "High": "Danger! Avoid consumption. Treat water or use alternative sources."
}

# -----------------------------
# Homepage
# -----------------------------
@app.route("/")
def home():
    return render_template_string("""
    <h1>Smart Water Quality Prediction API</h1>
    <p>Use POST /predict-risk with JSON data to get AI-predicted risk level.</p>
    <p>Example JSON:</p>
    <pre>
{
  "Temperature Min": 25, "Temperature Max": 30,
  "Dissolved Oxygen Min": 5, "Dissolved Oxygen Max": 8,
  "pH Min": 6.5, "pH Max": 7.5,
  "Conductivity Min": 150, "Conductivity Max": 250,
  "BOD Min": 2, "BOD Max": 4,
  "Nitrate Min": 1, "Nitrate Max": 3,
  "Fecal Coliform Min": 100, "Fecal Coliform Max": 250,
  "Total Coliform Min": 200, "Total Coliform Max": 400
}
    </pre>
    """)

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.route("/predict-risk", methods=["POST", "GET"])
def predict_risk():
    if request.method == "GET":
        return render_template_string("""
        <h2>Water Risk Prediction Endpoint</h2>
        <p>This endpoint only works with POST requests.</p>
        <p>Send JSON data as described on the homepage.</p>
        """)

    try:
        data = request.json
        df = pd.DataFrame([data], columns=numeric_cols)
        X_scaled = scaler.transform(df)
        y_pred = model.predict(X_scaled)
        risk_label = le.inverse_transform(y_pred)[0]

        return jsonify({
            "risk": risk_label,
            "guidance": guidance_dict[risk_label]
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
