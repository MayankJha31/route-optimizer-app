import pandas as pd
from sklearn.cluster import KMeans

def cluster_customers(df: pd.DataFrame, n_clusters: int = 2) -> pd.DataFrame:
    """
    Adds a 'Truck' column to the DataFrame by clustering customers into n groups.
    Each group corresponds to a delivery truck.
    """
    coords = df[['Latitude', 'Longitude']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Truck'] = kmeans.fit_predict(coords)
    return df
