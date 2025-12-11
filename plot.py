import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('XYZ_matrix.tsv', sep='\t', names=['x','y','frequency'])


plt.figure(figsize=(10, 6))


plt.gcf().set_facecolor('white')
scatter=plt.scatter(data['x'], data['y'], c=data['frequency'], s=50, alpha=0.6, cmap='inferno')
plt.colorbar(scatter, label='frequency')
plt.title('V-plot of nuclease fragments around TF binding sites')
plt.xlabel('Distance from protein center(bp)')
plt.ylabel('Fragment Size(bp)')
plt.ylim(40, 350)
plt.gca().set_facecolor('lightyellow')

plt.savefig("vplot.png", dpi=300, bbox_inches='tight')
plt.show()
