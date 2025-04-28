import matplotlib.pyplot as plt
import matplotlib as mplt
import numpy as np
#import mdshare
import pyemma
import glob
from pyemma.util.contexts import settings


pdb = '../inputs_pentapeptide/em_nowat.pdb'
files = glob.glob('Cycle1//all_traj.xtc')
torsions_feat = pyemma.coordinates.featurizer(pdb)
torsions_feat.add_backbone_torsions(cossin=True, periodic=False)
torsions_data = pyemma.coordinates.load(files, features=torsions_feat)
tica = pyemma.coordinates.tica(torsions_data, lag=5)
tica_output = tica.get_output()
tica_concatenated = np.concatenate(tica_output)


filec2 = glob.glob('Cycle2/all_traj.xtc')
torsions_featc2 = pyemma.coordinates.featurizer(pdb)
torsions_featc2.add_backbone_torsions(cossin=True, periodic=False)
torsions_datac2 = pyemma.coordinates.load(filec2, features=torsions_featc2)
ticac2 = pyemma.coordinates.tica(torsions_datac2, lag=5)
tica_outputc2 = ticac2.get_output()
tica_concatenatedc2 = np.concatenate(tica_outputc2)


filec3 = glob.glob('Cycle3/all_traj.xtc')
torsions_featc3 = pyemma.coordinates.featurizer(pdb)
torsions_featc3.add_backbone_torsions(cossin=True, periodic=False)
torsions_datac3 = pyemma.coordinates.load(filec3, features=torsions_featc3)
ticac3 = pyemma.coordinates.tica(torsions_datac3, lag=5)
tica_outputc3 = ticac3.get_output()
tica_concatenatedc3 = np.concatenate(tica_outputc3)

filec4 = glob.glob('Cycle4/all_traj.xtc')
torsions_featc4 = pyemma.coordinates.featurizer(pdb)
torsions_featc4.add_backbone_torsions(cossin=True, periodic=False)
torsions_datac4 = pyemma.coordinates.load(filec4, features=torsions_featc4)
ticac4 = pyemma.coordinates.tica(torsions_datac4, lag=5)
tica_outputc4 = ticac4.get_output()
tica_concatenatedc4 = np.concatenate(tica_outputc4)

filec5 = glob.glob('Cycle5//all_traj.xtc')
torsions_featc5 = pyemma.coordinates.featurizer(pdb)
torsions_featc5.add_backbone_torsions(cossin=True, periodic=False)
torsions_datac5 = pyemma.coordinates.load(filec5, features=torsions_featc5)
ticac5 = pyemma.coordinates.tica(torsions_datac5, lag=5)
tica_outputc5 = ticac5.get_output()
tica_concatenatedc5 = np.concatenate(tica_outputc5)


from sklearn.manifold import TSNE
tsne_model = TSNE(n_components=2, perplexity=30, random_state=42)
tica_tsnec = tsne_model.fit_transform(np.vstack(tica_concatenated))
tica_tsnec2 = tsne_model.fit_transform(np.vstack(tica_concatenatedc2))
tica_tsnec3 = tsne_model.fit_transform(np.vstack(tica_concatenatedc3))
tica_tsnec4 = tsne_model.fit_transform(np.vstack(tica_concatenatedc4))
tica_tsnec5 = tsne_model.fit_transform(np.vstack(tica_concatenatedc5))


import pyemma.plots as mplt
fig, axes = plt.subplots(1, 5, figsize=(25, 5))
levels = np.linspace(0.0, 5.0, 10)
with open('Cycle1/5unexplored_KDE_seperated.csv', 'r') as file1:
    highlight_framesc1 = [int(line.strip()) for line in file1 if line.strip().isdigit()]
with open('Cycle2/5unexplored_KDE_seperated.csv', 'r') as file2:
    highlight_framesc2 = [int(line.strip()) for line in file2 if line.strip().isdigit()]
with open('Cycle3/5unexplored_KDE_seperated.csv', 'r') as file3:
    highlight_framesc3 = [int(line.strip()) for line in file3 if line.strip().isdigit()]
with open('Cycle4/5unexplored_KDE_seperated.csv', 'r') as file4:
    highlight_framesc4 = [int(line.strip()) for line in file4 if line.strip().isdigit()]
with open('Cycle5/5unexplored_KDE_seperated.csv', 'r') as file5:
    highlight_framesc5 = [int(line.strip()) for line in file5 if line.strip().isdigit()]
mplt.plot_free_energy(tica_tsnec[:, 0], tica_tsnec[:, 1], ax=axes[0], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[0].scatter(tica_tsnec[highlight_framesc1, 0], tica_tsnec[highlight_framesc1, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec2[:, 0], tica_tsnec2[:, 1], ax=axes[1], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[1].scatter(tica_tsnec2[highlight_framesc2, 0], tica_tsnec2[highlight_framesc2, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec3[:, 0], tica_tsnec3[:, 1], ax=axes[2], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[2].scatter(tica_tsnec3[highlight_framesc3, 0], tica_tsnec3[highlight_framesc3, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec4[:, 0], tica_tsnec4[:, 1], ax=axes[3], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[3].scatter(tica_tsnec4[highlight_framesc4, 0], tica_tsnec4[highlight_framesc4, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec5[:, 0], tica_tsnec5[:, 1], ax=axes[4], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[4].scatter(tica_tsnec5[highlight_framesc5, 0], tica_tsnec5[highlight_framesc5, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')


axes[0].set_xlabel('tsne 1')
axes[0].set_ylabel('tsne 2')
axes[0].set_xlim(-100, 100)
axes[0].set_ylim(-100, 100)
axes[1].set_xlabel('tsne 1')
axes[1].set_ylabel('tsne 2')
axes[1].set_xlim(-100, 100)
axes[1].set_ylim(-100, 100)
axes[2].set_xlabel('tsne 1')
axes[2].set_ylabel('tsne 2')
axes[2].set_xlim(-100, 100)
axes[2].set_ylim(-100, 100)
axes[3].set_xlabel('tsne 1')
axes[3].set_ylabel('tsne 2')
axes[3].set_xlim(-100, 100)
axes[3].set_ylim(-100, 100)
axes[4].set_xlabel('tsne 1')
axes[4].set_ylabel('tsne 2')
axes[4].set_xlim(-100, 100)
axes[4].set_ylim(-100, 100)

plt.savefig("tsene1_ene.png" , dpi=300)


