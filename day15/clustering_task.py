from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Load Data 

from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=300, centers=5, cluster_std=0.60, random_state=0)
df = pd.DataFrame(X, columns=['Annual Income', 'Spending Score'])
print("Sample Data:\n", df.head())
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

wcss = [] 
for i in range(1, 11):
	kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
	kmeans.fit(X)
	wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)


plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
label='Centroids')
plt.title('Clusters of Users')
plt.legend()
plt.show()