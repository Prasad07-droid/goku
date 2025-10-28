import numpy as np 
import random 

def euclidean_distance(point1, point2): 
    """Calculate Euclidean distance between two points""" 
    return abs(point1 - point2) 

def kmeans(data, k=2, max_iterations=100): 
    """ 
    K-Means clustering algorithm 
    Parameters: - data: list of data points - k: number of clusters - max_iterations: maximum number of iterations 
    Returns: - centroids: final cluster centers - clusters: dictionary mapping cluster index to list of points 
    """ 
    centroids = random.sample(data, k) 
    print(f"Initial centroids: {centroids}\n") 
    
    for iteration in range(max_iterations): 
        clusters = {i: [] for i in range(k)} 
        
        for point in data: 
            distances = [euclidean_distance(point, centroid) for centroid in centroids] 
            closest_cluster = distances.index(min(distances)) 
            clusters[closest_cluster].append(point) 
        
        print(f"Iteration {iteration + 1}:") 
        print(f"Centroids: {centroids}") 
        for i, cluster_points in clusters.items(): 
            print(f"  Cluster {i + 1}: {sorted(cluster_points)}") 
        
        new_centroids = [] 
        for i in range(k): 
            if clusters[i]:  # Check if cluster is not empty 
                new_centroid = sum(clusters[i]) / len(clusters[i]) 
                new_centroids.append(new_centroid) 
            else: 
                new_centroids.append(centroids[i])  # Keep old centroid if cluster is empty 
        
        if new_centroids == centroids: 
            print("\nConverged!") 
            break 
            
        centroids = new_centroids 
        print() 
        
    return centroids, clusters 

data = [2, 4, 10, 12, 3, 20, 30, 11, 25] 

print("=" * 50) 
print("K-MEANS CLUSTERING") 
print("=" * 50) 
print(f"Data: {data}") 
print(f"Number of clusters (k): 2\n") 

final_centroids, final_clusters = kmeans(data, k=2) 

print("\n" + "=" * 50) 
print("FINAL RESULTS") 
print("=" * 50) 
print(f"Final centroids: {[round(c, 2) for c in final_centroids]}") 
for i, cluster_points in final_clusters.items(): 
    print(f"Cluster {i + 1}: {sorted(cluster_points)} (centroid: {round(final_centroids[i], 2)})")