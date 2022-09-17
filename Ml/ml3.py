import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

data, label = make_blobs( n_samples=300, centers=3, random_state=0, cluster_std=1 )

# fig = plt.figure( figsize=(10, 5) )
# ax1 = fig.add_subplot( 1, 2, 1 )
# colors = np.array( ["red", "blue", "green"] )
# ax1.scatter( data[:, 0], data[:, 1], color=colors[label], alpha=0.5 )
#
# kmeans = KMeans( n_clusters=3 )
# model = kmeans.fit( data )
# ax2 = fig.add_subplot( 1, 2, 2 )
# ax2.scatter( data[:, 0], data[:, 1], color=colors[model.labels_], alpha=0.5 )
# ax2.scatter( model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], color="k", marker="^" )
# plt.show()

# 엘보우기법
# from scipy.spatial.distance import cdist
# distortions = []
# ks = np.arange( 1, 11 )
# for k in ks :
#     kmeans = KMeans( n_clusters=k )
#     model = kmeans.fit( data )
#     distortions.append( 
#         sum( np.min( cdist( data, model.cluster_centers_, "euclidean" ), axis=1 ) ) / 300 )
# plt.plot( ks, distortions, "bx-" )
# plt.show()     

# 실루엣기법
kmeans = KMeans( n_clusters=3 )
model = kmeans.fit( data )
predicts = model.predict( data )
# # print( predicts )
# clust_labels = np.unique( predicts )        # [0, 1, 2]
# # print( clust_labels )
# n_cluster = clust_labels.shape[0]
# from sklearn.metrics import silhouette_samples
# from matplotlib import cm
# silhouette_values = silhouette_samples( data, predicts, metric="euclidean" )
# y_lower, y_upper = 0, 0
# yticks = []
# for i, cluster in enumerate( clust_labels ) :   # [0, 1, 2]
#     silhouette_cluster = silhouette_values[ predicts == cluster ]
#     # print( len( silhouette_cluster ) )
#     silhouette_cluster.sort()
#     y_upper += len( silhouette_cluster )
#     colors = cm.jet( float(i) / n_cluster )
#     plt.barh( range( y_lower, y_upper ), silhouette_cluster, height=0.1, edgecolor="none", color=colors )
#     yticks.append( ( y_upper + y_lower) / 2 )
#     y_lower += len( silhouette_cluster )
# silhouette_avg = np.mean( silhouette_values )    
# plt.axvline( silhouette_avg, color="k", linestyle="--" )
# plt.yticks( yticks, clust_labels+1 )
# plt.show()
    
from sklearn.metrics import confusion_matrix
result = confusion_matrix( predicts, label )
print( result )    


# DBSCAN #
from sklearn.datasets import make_moons
data, label = make_moons( n_samples=300, noise=0.05, random_state=0 )
kmeans = KMeans( n_clusters=2, random_state=0 )
model = kmeans.fit( data )
 
fig = plt.figure( figsize=( 10, 5 ) )
ax1 = fig.add_subplot( 1, 2, 1 )
colors = np.array( ["red", "blue"] )
ax1.scatter( data[:, 0], data[:, 1], color=colors[label], alpha=0.5 )

ax2 = fig.add_subplot( 1, 2, 2 )
ax2.scatter( data[:, 0], data[:, 1], color=colors[model.labels_], alpha=0.5 )

plt.show()



























