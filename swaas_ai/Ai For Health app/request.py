# request.py
import requests
import json

# Flask API endpoint
url = "http://127.0.0.1:5000/predict-risk"

# Example water quality parameters
data = {
    "Temperature\n?C (Min)": 25, "Temperature\n?C (Max)": 30,
    "Dissolved Oxygen (mg/L) (Min)": 5, "Dissolved Oxygen (mg/L) (Max)": 8,
    "pH (Min)": 6.5, "pH (Max)": 7.5,
    "Conductivity (?mhos/cm) (Min)": 150, "Conductivity (?mhos/cm) (Max)": 250,
    "BOD (mg/L) (Min)": 2, "BOD (mg/L) (Max)": 4,
    "Nitrate N + Nitrite N(mg/L) (Min)": 1, "Nitrate N + Nitrite N(mg/L) (Max)": 3,
    "Fecal Coliform (MPN/100ml) (Min)": 100, "Fecal Coliform (MPN/100ml) (Max)": 250,
    "Total Coliform (MPN/100ml) (Min)": 200, "Total Coliform (MPN/100ml) (Max)": 400
}

try:
    # Send POST request with JSON data
    response = requests.post(url, json=data)
    
    # Raise error if request failed
    response.raise_for_status()
    
    # Print the JSON response from the API
    result = response.json()
    print(json.dumps(result, indent=4))
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
