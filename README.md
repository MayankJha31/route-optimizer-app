# 🚚 Dairy Logistics Route Optimizer

This app optimizes delivery routes for a dairy company by dividing 50 customer locations between 2 trucks using clustering and solving TSP (Traveling Salesman Problem) for each.

---

## ⚙️ Setup Instructions

1. **Clone the repo**

git clone https://github.com/MayankJha31/route-optimizer-app.git
cd route-optimizer-app
python -m venv venv
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
streamlit run app/main.py
streamlit run app/main.py


## Approach

CSV Upload – User uploads customer data.

Clustering – KMeans (k=2) clusters customers for 2 trucks.

TSP Optimization – Google OR-Tools calculates shortest route for each truck (start & end at warehouse).

Visualization – Shows tables, distances, and route maps using Folium.

## Input
CustomerID,BusinessName,Latitude,Longitude
101,Milk Point A,23.0300,72.5800
102,Dairy Corner B,23.0201,72.5650


## Output
1. Two trucks with optimized customer routes

2. Route distance in km

3. Interactive map visualization

🔗 Live Demo.
Deployed on Streamlit: [streamlit.io] (https://route-optimizer-app-nav6rjzph6mkyhh9mgism7.streamlit.app/)
```bash
