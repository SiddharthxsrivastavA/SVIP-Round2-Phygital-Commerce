import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def recommend_products(customer_id, unified_data_path):
    data = pd.read_csv(unified_data_path)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data.drop(['customer_id', 'purchase_history'], axis=1))
    
    kmeans = KMeans(n_clusters=5)
    data['cluster'] = kmeans.fit_predict(data_scaled)
    
    customer_cluster = data.loc[data['customer_id'] == customer_id, 'cluster'].values[0]
    recommendations = data[data['cluster'] == customer_cluster].sample(5)['product_id'].values
    return recommendations

if __name__ == "__main__":
    customer_id = 12345
    recommendations = recommend_products(customer_id, 'data/unified_customer_data.csv')
    print(f"Recommended products for customer {customer_id}: {recommendations}")
