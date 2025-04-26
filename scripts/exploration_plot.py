%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#import mdshare
import pyemma
import glob
from pyemma.util.contexts import settings

fig, axes = plt.subplots(1, 5, figsize=(25, 5))
levels = np.linspace(0.0, 5.0, 10)
with open('cycle1/5unexplored_KDE_seperated.csv', 'r') as file1:
    highlight_framesc1 = [int(line.strip()) for line in file1 if line.strip().isdigit()]
with open('cycle2/5unexplored_KDE_seperated.csv', 'r') as file2:
    highlight_framesc2 = [int(line.strip()) for line in file2 if line.strip().isdigit()]
with open('cycle3/5unexplored_KDE_seperated.csv', 'r') as file3:
    highlight_framesc3 = [int(line.strip()) for line in file3 if line.strip().isdigit()]
with open('cycle4/5unexplored_KDE_seperated.csv', 'r') as file4:
    highlight_framesc4 = [int(line.strip()) for line in file4 if line.strip().isdigit()]
with open('cycle5/5unexplored_KDE_seperated.csv', 'r') as file5:
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
ax.set_title('Free Energy on tsne projection')
plt.savefig("tsene1_ene.png" , dpi=300)


fig, axes = plt.subplots(1, 5, figsize=(25, 5))
levels = np.linspace(0.0, 5.0, 10)

with open('cycle6/5unexplored_KDE_seperated.csv', 'r') as file1:
    highlight_framesc1 = [int(line.strip()) for line in file1 if line.strip().isdigit()]
with open('cycle7/5unexplored_KDE_seperated.csv', 'r') as file2:
    highlight_framesc2 = [int(line.strip()) for line in file2 if line.strip().isdigit()]
with open('cycle8/5unexplored_KDE_seperated.csv', 'r') as file3:
    highlight_framesc3 = [int(line.strip()) for line in file3 if line.strip().isdigit()]
with open('cycle9/5unexplored_KDE_seperated.csv', 'r') as file4:
    highlight_framesc4 = [int(line.strip()) for line in file4 if line.strip().isdigit()]
#with open('cycle10/5unexplored_KDE_seperated.csv', 'r') as file5:
 #   highlight_framesc5 = [int(line.strip()) for line in file5 if line.strip().isdigit()]
mplt.plot_free_energy(tica_tsnec6[:, 0], tica_tsnec6[:, 1], ax=axes[0], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[0].scatter(tica_tsnec6[highlight_framesc1, 0], tica_tsnec6[highlight_framesc1, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec7[:, 0], tica_tsnec7[:, 1], ax=axes[1], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[1].scatter(tica_tsnec7[highlight_framesc2, 0], tica_tsnec7[highlight_framesc2, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec8[:, 0], tica_tsnec8[:, 1], ax=axes[2], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[2].scatter(tica_tsnec8[highlight_framesc3, 0], tica_tsnec8[highlight_framesc3, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec9[:, 0], tica_tsnec9[:, 1], ax=axes[3], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
axes[3].scatter(tica_tsnec9[highlight_framesc4, 0], tica_tsnec9[highlight_framesc4, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')
mplt.plot_free_energy(tica_tsnec10[:, 0], tica_tsnec10[:, 1], ax=axes[4], vmin=0.0, vmax=5.0, levels=levels, cbar=True)
#axes[0].scatter(tica_tsnec10[highlight_framesc1, 0], tica_tsnec10[highlight_framesc1, 1], color='red', label='Highlighted Frames', s=50, edgecolor='black', linewidth=1.5, marker='x')


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
ax.set_title('Free Energy on tsne projection')
plt.savefig("tsene2_ene.png" , dpi=300)
