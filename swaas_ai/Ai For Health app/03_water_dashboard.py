import pandas as pd
import dash
from dash import dcc, html, Output, Input
import plotly.express as px
import requests

# -----------------------------
# 1️⃣ Load water quality data
# -----------------------------
file_path = r"C:\Users\HP\water_quality\Water_pond_tanks_2021.csv"
df = pd.read_csv(file_path, encoding='cp1252', low_memory=False)

# -----------------------------
# 2️⃣ Setup Dash
# -----------------------------
app = dash.Dash(__name__)
server = app.server

# Parameters to choose from
parameters = ['Temperature Min', 'Temperature Max', 'Dissolved Oxygen Min', 'Dissolved Oxygen Max',
              'pH Min', 'pH Max', 'Conductivity Min', 'Conductivity Max', 'BOD Min', 'BOD Max',
              'Nitrate Min', 'Nitrate Max', 'Fecal Coliform Min', 'Fecal Coliform Max',
              'Total Coliform Min', 'Total Coliform Max']

API_URL = "http://127.0.0.1:5000/predict-risk"

# -----------------------------
# Helper function to get risk from API
# -----------------------------
def get_risk_from_api(row):
    data = {param: row[param] for param in parameters}
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            result = response.json()
            return result.get("risk", "Low"), result.get("guidance", "")
        else:
            return "Low", ""
    except:
        return "Low", ""

# -----------------------------
# Precompute risks for top 50 rows (for demo)
# -----------------------------
df_risk = df.head(50).copy()
df_risk[['Risk', 'Guidance']] = df_risk.apply(lambda row: pd.Series(get_risk_from_api(row)), axis=1)

color_map = {"Low": "green", "Moderate": "yellow", "High": "red"}
df_risk['RiskColor'] = df_risk['Risk'].map(color_map)

# -----------------------------
# 3️⃣ Layout
# -----------------------------
app.layout = html.Div([
    html.H1("Smart Water Quality Dashboard"),
    html.Label("Select Parameter:"),
    dcc.Dropdown(
        id='parameter-dropdown',
        options=[{'label': p, 'value': p} for p in parameters],
        value='BOD Min'
    ),
    dcc.Graph(id='risk-bar-chart'),
    html.H2("Alerts & Guidance"),
    html.Div(id='alerts-table')
])

# -----------------------------
# 4️⃣ Callbacks
# -----------------------------
@app.callback(
    Output('risk-bar-chart', 'figure'),
    Output('alerts-table', 'children'),
    Input('parameter-dropdown', 'value')
)
def update_dashboard(selected_param):
    # Bar chart
    fig = px.bar(df_risk, x='Name of Monitoring Location', y=selected_param,
                 color='Risk', color_discrete_map=color_map,
                 title=f"{selected_param} Levels & Risk")
    
    # Alerts table
    table = html.Table([
        html.Tr([html.Th("Location"), html.Th("Risk"), html.Th("Guidance")])] +
        [html.Tr([
            html.Td(row['Name of Monitoring Location']),
            html.Td(row['Risk'], style={'color': row['RiskColor'], 'font-weight':'bold'}),
            html.Td(row['Guidance'])
        ]) for _, row in df_risk.iterrows()]
    )
    
    return fig, table

# -----------------------------
# 5️⃣ Run dashboard
# -----------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
