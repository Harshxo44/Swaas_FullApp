import pandas as pd, numpy as np, joblib
from math import radians, sin, cos, asin, sqrt
from pathlib import Path

DATA = pd.read_csv(r".\water_quality\water_quality_with_risk.csv")
# Try to detect location columns, if any
lat_col = next((c for c in DATA.columns if c in ["lat","latitude","y","lat_deg"]), None)
lon_col = next((c for c in DATA.columns if c in ["lon","longitude","x","lon_deg"]), None)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return 2*R*asin(sqrt(a))

def nearest_site(lat, lon):
    if not (lat_col and lon_col):
        return None  # dataset has no geocoordinates
    dists = DATA.apply(lambda r: haversine(lat, lon, r[lat_col], r[lon_col]), axis=1)
    idx = int(np.argmin(dists))
    return DATA.iloc[idx].to_dict()

def predict_from_row(row_dict):
    # If you trained the RF:
    model_path = Path(r".\water_quality\water_unsafe_rf.pkl")
    feats_path  = Path(r".\water_quality\feature_order.pkl")
    if not (model_path.exists() and feats_path.exists()):
        # fall back to rule-based risk already in CSV
        return {
            "risk_score": row_dict.get("risk_score", None),
            "risk_level": row_dict.get("risk_level", None),
            "unsafe_pred": int(row_dict.get("risk_level","Low")=="High")
        }
    clf = joblib.load(model_path)
    feat_order = joblib.load(feats_path)

    row = {k: row_dict.get(k, 0) for k in feat_order}
    import numpy as np
    X = np.array([list(row.values())])
    pred = int(clf.predict(X)[0])
    return {
        "risk_score": row_dict.get("risk_score", None),
        "risk_level": row_dict.get("risk_level", None),
        "unsafe_pred": pred
    }

# Demo
if __name__ == "__main__":
    # Example: pick the first row
    d = DATA.iloc[0].to_dict()
    print("Example row risk:", predict_from_row(d))

    # If you have lat/lon from the app:
    example = nearest_site(lat=26.9, lon=94.1)  # (replace with actual GPS)
    if example:
        print("Nearest site result:", predict_from_row(example))
    else:
        print("No geocoordinates in dataset; use admin/district filters instead.")
