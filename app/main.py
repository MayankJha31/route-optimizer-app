import streamlit as st
import pandas as pd

from clustering import cluster_customers
from route_optimizer import solve_tsp
from map_visualizer import generate_map

st.set_page_config(page_title="Logistics Route Optimizer", layout="wide")

st.title("🚚 Dairy Logistics Route Optimizer")
st.markdown("""
This app divides 50 customers between 2 delivery trucks and calculates the most efficient route for each truck using Google OR-Tools and KMeans clustering.
""")

# Upload your CSV file
uploaded_file = st.file_uploader("📤 Upload customer CSV file", type=["csv"])
if uploaded_file:
    # Load and clean the data
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove whitespace from column names

    # Rename columns if needed to expected format
    rename_map = {
        "Customer ID": "CustomerID",
        "Business Name": "BusinessName",
        "Latitude": "Latitude",
        "Longitude": "Longitude"
    }
    df.rename(columns=rename_map, inplace=True)

    # Show debug info for column names
    st.write("📋 Columns in uploaded file:", df.columns.tolist())

    # Define required columns
    required_cols = ['CustomerID', 'BusinessName', 'Latitude', 'Longitude']
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        st.error(f"❌ The following required columns are missing in the uploaded CSV: {missing_cols}")
        st.stop()

    # 📍 Set Warehouse Coordinates
    warehouse = {
        "lat": 23.0225,  # Replace with actual warehouse latitude
        "lon": 72.5714   # Replace with actual warehouse longitude
    }

    # 🧠 Step 1: Cluster customers for 2 trucks
    df = cluster_customers(df)

    # 🛣 Step 2: Solve TSP route for Truck 1
    st.subheader("🚛 Truck 1 Route")
    truck1_df = df[df['Truck'] == 0].reset_index(drop=True)
    route1, dist1 = solve_tsp(truck1_df, warehouse)
    st.write(f"Total Distance: **{dist1:.2f} km**")
    st.dataframe(truck1_df[['CustomerID', 'BusinessName', 'Latitude', 'Longitude']])

    # 🛣 Step 3: Solve TSP route for Truck 2
    st.subheader("🚛 Truck 2 Route")
    truck2_df = df[df['Truck'] == 1].reset_index(drop=True)
    route2, dist2 = solve_tsp(truck2_df, warehouse)
    st.write(f"Total Distance: **{dist2:.2f} km**")
    st.dataframe(truck2_df[['CustomerID', 'BusinessName', 'Latitude', 'Longitude']])

    # 🗺 Step 4: Show interactive route map
    st.subheader("🗺 Route Map")
    html_map = generate_map(df, warehouse, route1, route2)
    st.components.v1.html(html_map, height=600)

else:
    st.info("Please upload your `customers.csv` file to begin.")
