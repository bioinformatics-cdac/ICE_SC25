import mdtraj as md
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import hdbscan
#from sklearn.cluster import DBSCAN, HDBSCAN
from collections import Counter
from sklearn.manifold import TSNE

# Paths to Trajectories for Each Method
methods = ['random', 'kmeans', 'kde', 'iforest_kmeans', 'combined']
trajectory_paths = {
    'random': 'moreruns_random/cycle10/all_traj.xtc',
    'kmeans': 'moreruns_kmeans/cycle9/all_traj.xtc',
    'kde': 'moreruns_kde/cycle10/all_traj.xtc',
    'iforest_kmeans': 'moreruns/cycle10/all_traj.xtc',
    'combined': 'moreruns_all3/cycle10/all_traj.xtc'
}
topology = 'em_nowat.pdb'

# Output Directory
output_dir = 'comparison_outputs_text'
os.makedirs(output_dir, exist_ok=True)

def featurize(traj):
    phi = md.compute_phi(traj)[1]
    psi = md.compute_psi(traj)[1]
    distances = md.compute_distances(traj, [[0, 1], [1, 2], [2, 3], [3, 4]])
    features = np.concatenate((phi, psi, distances), axis=1)
    return features

def dimensionality_reduction(features, n_components=8):
    pca = PCA(n_components=n_components)
    reduced = pca.fit_transform(features)
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    tsne_transformed = tsne.fit_transform(reduced)
    return tsne_transformed

def cluster_data(data):
    clusterer = hdbscan.HDBSCAN(min_cluster_size=75, metric='euclidean')
    labels = clusterer.fit_predict(data)
    return labels

def coverage_metric(labels):
    return len(set(labels) - {-1})

def rare_states(labels, threshold=0.05):
    counts = Counter(labels)
    total = len(labels)
    rare_clusters = [k for k, v in counts.items() if v / total < threshold and k != -1]
    return len(rare_clusters)

def saturation_curve(labels):
    discovered = set()
    saturation = []
    for i, label in enumerate(labels):
        if label != -1:
            discovered.add(label)
        saturation.append(len(discovered))
    return saturation

all_metrics = {}

# Loop through each method
for method in methods:
    print(f"Processing {method}...")
    traj = md.load(trajectory_paths[method], top=topology)
    features = featurize(traj)
    reduced = dimensionality_reduction(features)
    labels = cluster_data(reduced)

    coverage = coverage_metric(labels)
    rare = rare_states(labels)
    saturation = saturation_curve(labels)

    all_metrics[method] = {
        'coverage': coverage,
        'rare_states': rare,
        'saturation': saturation
    }

    # Save metrics to file
    with open(os.path.join(output_dir, f"{method}_metrics.txt"), 'w') as f:
        f.write(f"Coverage: {coverage}\n")
        f.write(f"Rare States: {rare}\n")

    with open(os.path.join(output_dir, f"{method}_satura.txt"), 'w') as m:
        m.write(f"Saturation: {saturation}\n")



    # Plot Saturation Curve
    plt.plot(saturation, label=method)

# Plot Final Saturation Curves
plt.title("Saturation Curves of Different Methods")
plt.xlabel("Frames")
plt.ylabel("Unique Clusters Discovered")
plt.legend()
plt.savefig(os.path.join(output_dir, "saturation_curves.png"))
plt.close()

# Summary Plot for Coverage and Rare States
methods_list = list(all_metrics.keys())
coverage_scores = [all_metrics[m]['coverage'] for m in methods_list]
rare_scores = [all_metrics[m]['rare_states'] for m in methods_list]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].bar(methods_list, coverage_scores, color='skyblue')
ax[0].set_title("Coverage Metric")
ax[0].set_ylabel("Number of Unique Clusters")

ax[1].bar(methods_list, rare_scores, color='lightcoral')
ax[1].set_title("Rare States Found")
ax[1].set_ylabel("Number of Rare States")

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "comparison_summary.png"))
plt.close()

print("All metrics and plots saved successfully!")

