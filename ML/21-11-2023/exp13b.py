from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data=load_breast_cancer()
x=data.data
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(x)
cluster_labels = kmeans.labels_
print(cluster_labels)
centroids=kmeans.cluster_centers_
print(centroids)
plt.scatter(x[:,0],x[:,1],c=cluster_labels,cmap="viridis",marker="o",edgecolors='black')
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=200,marker="*",label="Centroids")
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.title("KMeans clustering of loadbreastcancer dataset")
plt.legend()
plt.show()